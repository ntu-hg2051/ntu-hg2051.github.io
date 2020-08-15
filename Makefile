
# Repository settings
REPO := $(shell git config --get remote.origin.url)
BRANCH = gh-pages

# Pandoc parameters
TEMPLATE = --template "templates/main"
CSS = -c "css/main.css"

# Find sources and determine targets
INDEX := $(BRANCH)/index.html
SOURCES := $(shell find src/ -name '*.md')
TARGETS := $(addprefix $(BRANCH)/,$(patsubst src/%,%,$(SOURCES:%.md=%.html)))

SASSFILES = $(wildcard css/*.scss)
CSSFILES = $(addprefix $(BRANCH)/,$(SASSFILES:%.scss=%.css))

STATICFILES = $(addprefix $(BRANCH)/,$(wildcard static/*))

all: init clean html commit

html: $(CSSFILES) $(STATICFILES) $(INDEX) $(TARGETS)

$(INDEX): index.md templates/index.html5
	pandoc -s --template "templates/index" $(CSS) -f markdown -t html5 -o "$@" "$<"

$(BRANCH)/%.html: src/%.md
	pandoc -s $(TEMPLATE) --toc $(CSS) -f markdown --highlight-style pygments -t html5 -o "$@" "$<"

$(BRANCH)/css/%.css: css/%.scss
	sass "$<" "$@"

$(BRANCH)/static/%: static/%
	cp "$<" "$@"

$(BRANCH):
	git clone "$(REPO)" "$(BRANCH)"
	(cd $(BRANCH) && git checkout $(BRANCH)) || (cd $(BRANCH) && git checkout --orphan $(BRANCH) && git rm -rf .)
	mkdir -p $(BRANCH)/css
	mkdir -p $(BRANCH)/static

serve:
	cd $(BRANCH) && python3 -m http.server

commit:
	cd $(BRANCH) && \
	   git add . && \
	   git commit --edit --message="Publish @$$(date)"
	cd $(BRANCH) && \
	   git push origin $(BRANCH)

clean:
	rm -rf "$(BRANCH)"

.PHONY: html clean
