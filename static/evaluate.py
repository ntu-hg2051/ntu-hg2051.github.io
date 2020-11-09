from itertools import zip_longest

def load(path):
    """Load annotated sentences from a file."""
    sentence = []  # sentence should always be the last sentence in sentences
    sentences = [sentence]
    with open(path, encoding='utf-8') as file:
        for line in file:
            if line.strip() == '':  # a blank line; make a new sentence
                sentence = []
                sentences.append(sentence)
            else:
                # partition() is similar to split(), but always returns a triple
                words, _, label = line.partition('\t')
                words = tuple(words.split())  # len(words) may be > 1 for MWEs
                label = label.rstrip()  # remove any trailing space (including newlines)
                if not label:
                    label = None
                sentence.append((words, label))
    # filter out empty sentences (e.g., from blank line at beginning/end of file)
    return [sent for sent in sentences if sent]


def flatten_sentence(sentence):
    """Flatten MWEs in a sentence."""
    new_sentence = []
    for words, label in sentence:
        if len(words) > 1:
            new_sentence.extend(zip(words, [label] * len(words)))
        else:
            new_sentence.append((words[0], label))
    return new_sentence


def evaluate(gold, sys):
    # validate files contain equal numbers of sentences
    if len(gold) != len(sys):
        print(f'warning: different number of gold ({len(gold)}) '
              f'and system ({len(sys)}) sentences')
    # gold_tokens  -> number of tokens in gold file
    # sys_tokens   -> number of tokens in sys file
    # skipped      -> number of tokens that were not compared
    gold_tokens = sys_tokens = skipped = 0
    # gold_labels -> number of labels in gold file
    # sys_labels  -> number of labels in sys file
    # matching    -> number of labels that are the same in both
    gold_labels = sys_labels = matching = 0
    for i, (gold_sent, sys_sent) in enumerate(zip(gold, sys), 1):
        gold_sent = flatten_sentence(gold_sent)
        sys_sent = flatten_sentence(sys_sent)

        gold_tokens += len(gold_sent)
        sys_tokens += len(sys_sent)

        gold_labels += sum(1 for _, label in gold_sent if label)
        sys_labels += sum(1 for _, label in sys_sent if label)

        skip = False

        for j, (gold_inst, sys_inst) in enumerate(zip_longest(gold_sent, sys_sent), 1):
            gold_word, gold_label = gold_inst if gold_inst is not None else (None, None)
            sys_word, sys_label = sys_inst if sys_inst is not None else (None, None)

            # validate each sentence has the same words (when flattened)
            if skip or gold_word != sys_word:
                skipped += 1
                if not skip:
                    print(f'tokens are not aligned in sentence {i}, index {j}: '
                          f'{gold_word!r} != {sys_word!r}')
                    print('skipping remaining tokens')
                    skip = True
                continue

            if gold_label and gold_label == sys_label:
                matching += 1

    precision = matching / sys_labels
    recall = matching / gold_labels
    fscore = 2 * ((precision * recall) / (precision + recall))
    print('Totals:')
    print(f'  Gold tokens   : {gold_tokens:>6}')
    print(f'  System tokens : {sys_tokens:>6}')
    print(f'  Skipped tokens: {skipped:>6}')
    print(f'  Gold labels   : {gold_labels:>6}')
    print(f'  System labels : {sys_labels:>6}')
    print(f'  Matched labels: {matching:>6}')
    print('Scores:')
    print(f'  Precision: {precision:4.2g}  ({matching} / {sys_labels})')
    print(f'  Recall   : {recall:4.2g}  ({matching} / {gold_labels})')
    print(f'  F-score  : {fscore:4.2g}  (2PR / (P + R))')
    # print(f'  Accuracy : {(matching + true_negatives) / total_tokens:4.2g}')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('gold', help='gold evaluation data')
    parser.add_argument('sys', help='system output data')
    args = parser.parse_args()

    gold = load(args.gold)
    sys = load(args.sys)
    evaluate(gold, sys)
