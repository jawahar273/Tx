# Minimal makefile for Sphinx documentation
#

config:
	export CONFIG = config.docs_local

# You can set these variables from the command line.
CONFIG        = config.docs_local
EXPORT 		  = export
SPHINXOPTS    =
SPHINXBUILD   = python -msphinx
SPHINXPROJ    = Tx, TxBot
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
