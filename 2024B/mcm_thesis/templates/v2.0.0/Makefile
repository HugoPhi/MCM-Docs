# Makefile for LaTeX Project

# 文件名（不带扩展名）
TEXFILE = main

# 目标文件夹
BUILDDIR = build

# 输入文件夹
FIGURESDIR = figures
CODEDIR = code
SRC = src  # 子章节存放的目录

# 编译命令
LATEX = pdflatex -shell-escape -interaction=nonstopmode
BIBTEX = biber

# 输出文件
PDF = $(BUILDDIR)/$(TEXFILE).pdf
LOG = $(BUILDDIR)/$(TEXFILE).log
AUX = $(BUILDDIR)/$(TEXFILE).aux
BIB = $(BUILDDIR)/ref.bib

# 创建build目录和src目录
$(shell mkdir -p $(BUILDDIR)/src)

# 默认目标
all: $(PDF)

# 生成PDF
$(PDF): $(TEXFILE).tex $(BUILDDIR)/$(TEXFILE).bib $(BUILDDIR)/src/*.tex
	@echo "Compiling LaTeX file..."
	$(LATEX) -output-directory=$(BUILDDIR) $(TEXFILE).tex
	$(BIBTEX) $(BUILDDIR)/$(TEXFILE)
	$(LATEX) -output-directory=$(BUILDDIR) $(TEXFILE).tex
	$(LATEX) -output-directory=$(BUILDDIR) $(TEXFILE).tex
	@echo "Build finished. Output: $(PDF)"

# 拷贝.bib文件到build目录
$(BUILDDIR)/$(TEXFILE).bib: ref.bib
	@echo "Copying bib file..."
	cp ref.bib $(BUILDDIR)

# 拷贝子章节到build目录
$(BUILDDIR)/src/%.tex: $(SRC)/%.tex
	@echo "Copying $< to build directory..."
	cp $< $(BUILDDIR)/src

# 拷贝图像到build目录
$(BUILDDIR)/$(FIGURESDIR)/%: $(FIGURESDIR)/%
	@echo "Copying figure: $<"
	cp $< $(BUILDDIR)/$(FIGURESDIR)

# 清理目标
clean:
	@echo "Cleaning build files..."
	rm -rf \
		$(BUILDDIR)/*.aux \
		$(BUILDDIR)/*.bbl \
		$(BUILDDIR)/*.blg \
		$(BUILDDIR)/*.log \
		$(BUILDDIR)/*.out \
		$(BUILDDIR)/*.bcf \
		$(BUILDDIR)/*.xml \
		$(BUILDDIR)/*.toc \
		$(BUILDDIR)/*.bib \
		$(BUILDDIR)/$(FIGURESDIR)/*.pdf \
		$(PDF)

# 伪目标
.PHONY: all clean
