# revision 28213
# category Package
# catalog-ctan /macros/latex/contrib/hyperref
# catalog-date 2012-11-08 00:51:05 +0100
# catalog-license lppl
# catalog-version 6.83m
Name:		texlive-hyperref
Version:	6.83m
Release:	1
Summary:	Extensive support for hypertext in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hyperref
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyperref.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyperref.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyperref.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The hyperref package is used to handle cross-referencing
commands in LaTeX to produce hypertext links in the document.
The package provides backends for the \special set defined for
HyperTeX DVI processors; for embedded pdfmark commands for
processing by Acrobat Distiller (dvips and Y&Y's dvipsone); for
Y&Y's dviwindo; for PDF control within pdfTeX and dvipdfm; for
TeX4ht; and for VTeX's pdf and HTML backends. The package is
distributed with the backref and nameref packages, which make
use of the facilities of hyperref. The package depends on the
author's kvoptions, ltxcmdsand refcount packages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hyperref/backref.sty
%{_texmfdistdir}/tex/latex/hyperref/hdvipdfm.def
%{_texmfdistdir}/tex/latex/hyperref/hdvips.def
%{_texmfdistdir}/tex/latex/hyperref/hdvipson.def
%{_texmfdistdir}/tex/latex/hyperref/hdviwind.def
%{_texmfdistdir}/tex/latex/hyperref/hpdftex.def
%{_texmfdistdir}/tex/latex/hyperref/htex4ht.cfg
%{_texmfdistdir}/tex/latex/hyperref/htex4ht.def
%{_texmfdistdir}/tex/latex/hyperref/htexture.def
%{_texmfdistdir}/tex/latex/hyperref/hvtex.def
%{_texmfdistdir}/tex/latex/hyperref/hvtexhtm.def
%{_texmfdistdir}/tex/latex/hyperref/hvtexmrk.def
%{_texmfdistdir}/tex/latex/hyperref/hxetex.def
%{_texmfdistdir}/tex/latex/hyperref/hylatex.ltx
%{_texmfdistdir}/tex/latex/hyperref/hyperref.sty
%{_texmfdistdir}/tex/latex/hyperref/hypertex.def
%{_texmfdistdir}/tex/latex/hyperref/minitoc-hyper.sty
%{_texmfdistdir}/tex/latex/hyperref/nameref.sty
%{_texmfdistdir}/tex/latex/hyperref/nohyperref.sty
%{_texmfdistdir}/tex/latex/hyperref/ntheorem-hyper.sty
%{_texmfdistdir}/tex/latex/hyperref/pd1enc.def
%{_texmfdistdir}/tex/latex/hyperref/pdfmark.def
%{_texmfdistdir}/tex/latex/hyperref/psdextra.def
%{_texmfdistdir}/tex/latex/hyperref/puarenc.def
%{_texmfdistdir}/tex/latex/hyperref/puenc.def
%{_texmfdistdir}/tex/latex/hyperref/puvnenc.def
%{_texmfdistdir}/tex/latex/hyperref/xr-hyper.sty
%doc %{_texmfdistdir}/doc/latex/hyperref/ChangeLog
%doc %{_texmfdistdir}/doc/latex/hyperref/ChangeLog.pdf
%doc %{_texmfdistdir}/doc/latex/hyperref/README
%doc %{_texmfdistdir}/doc/latex/hyperref/README.pdf
%doc %{_texmfdistdir}/doc/latex/hyperref/backref.pdf
%doc %{_texmfdistdir}/doc/latex/hyperref/cmmi10-22.gif
%doc %{_texmfdistdir}/doc/latex/hyperref/cmsy10-21.gif
%doc %{_texmfdistdir}/doc/latex/hyperref/hyperref.pdf
%doc %{_texmfdistdir}/doc/latex/hyperref/manual.css
%doc %{_texmfdistdir}/doc/latex/hyperref/manual.html
%doc %{_texmfdistdir}/doc/latex/hyperref/manual.pdf
%doc %{_texmfdistdir}/doc/latex/hyperref/manual2.html
%doc %{_texmfdistdir}/doc/latex/hyperref/manual3.html
%doc %{_texmfdistdir}/doc/latex/hyperref/nameref.pdf
%doc %{_texmfdistdir}/doc/latex/hyperref/options.pdf
%doc %{_texmfdistdir}/doc/latex/hyperref/paper.pdf
%doc %{_texmfdistdir}/doc/latex/hyperref/slides.pdf
#- source
%doc %{_texmfdistdir}/source/latex/hyperref/backref.dtx
%doc %{_texmfdistdir}/source/latex/hyperref/bmhydoc.sty
%doc %{_texmfdistdir}/source/latex/hyperref/doc/fdl.tex
%doc %{_texmfdistdir}/source/latex/hyperref/doc/manual.tex
%doc %{_texmfdistdir}/source/latex/hyperref/doc/options.tex
%doc %{_texmfdistdir}/source/latex/hyperref/hyperref.dtx
%doc %{_texmfdistdir}/source/latex/hyperref/hyperref.ins
%doc %{_texmfdistdir}/source/latex/hyperref/nameref.dtx
%doc %{_texmfdistdir}/source/latex/hyperref/psdmapshortnames.pl
%doc %{_texmfdistdir}/source/latex/hyperref/test/Makefile
%doc %{_texmfdistdir}/source/latex/hyperref/test/bit.tex
%doc %{_texmfdistdir}/source/latex/hyperref/test/hog.eps
%doc %{_texmfdistdir}/source/latex/hyperref/test/hog.pdf
%doc %{_texmfdistdir}/source/latex/hyperref/test/phys1.jpg
%doc %{_texmfdistdir}/source/latex/hyperref/test/phys2.jpg
%doc %{_texmfdistdir}/source/latex/hyperref/test/picture.eps
%doc %{_texmfdistdir}/source/latex/hyperref/test/picture.pdf
%doc %{_texmfdistdir}/source/latex/hyperref/test/picture.png
%doc %{_texmfdistdir}/source/latex/hyperref/test/test-bm-pu-licr.tex
%doc %{_texmfdistdir}/source/latex/hyperref/test/test0.tex
%doc %{_texmfdistdir}/source/latex/hyperref/test/test1.tex
%doc %{_texmfdistdir}/source/latex/hyperref/test/test2.tex
%doc %{_texmfdistdir}/source/latex/hyperref/test/test3.tex
%doc %{_texmfdistdir}/source/latex/hyperref/test/test4.tex
%doc %{_texmfdistdir}/source/latex/hyperref/test/test6.tex
%doc %{_texmfdistdir}/source/latex/hyperref/test/test7.tex
%doc %{_texmfdistdir}/source/latex/hyperref/test/test8.tex
%doc %{_texmfdistdir}/source/latex/hyperref/test/testams.tex
%doc %{_texmfdistdir}/source/latex/hyperref/test/testbib.bbl
%doc %{_texmfdistdir}/source/latex/hyperref/test/testbib.bib
%doc %{_texmfdistdir}/source/latex/hyperref/test/testbib.tex
%doc %{_texmfdistdir}/source/latex/hyperref/test/testbmgl.tex
%doc %{_texmfdistdir}/source/latex/hyperref/test/testbmu.tex
%doc %{_texmfdistdir}/source/latex/hyperref/test/testbookmark.tex
%doc %{_texmfdistdir}/source/latex/hyperref/test/testfor2.tex
%doc %{_texmfdistdir}/source/latex/hyperref/test/testform.tex
%doc %{_texmfdistdir}/source/latex/hyperref/test/testinfo.tex
%doc %{_texmfdistdir}/source/latex/hyperref/test/testnb.tex
%doc %{_texmfdistdir}/source/latex/hyperref/test/testoz.tex
%doc %{_texmfdistdir}/source/latex/hyperref/test/testslide.tex
%doc %{_texmfdistdir}/source/latex/hyperref/test/testurl.bbl
%doc %{_texmfdistdir}/source/latex/hyperref/test/testurl.bib
%doc %{_texmfdistdir}/source/latex/hyperref/test/testurl.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
