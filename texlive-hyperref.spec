%global tl_name hyperref
%global tl_revision 79408

Name:		texlive-%{tl_name}
Epoch:		1
Version:	7.01r
Release:	%{tl_revision}.1
Summary:	Extensive support for hypertext in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hyperref
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyperref.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyperref.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyperref.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Requires:	texlive(atbegshi)
Requires:	texlive(auxhook)
Requires:	texlive(bitset)
Requires:	texlive(etexcmds)
Requires:	texlive(gettitlestring)
Requires:	texlive(hycolor)
Requires:	texlive(iftex)
Requires:	texlive(infwarerr)
Requires:	texlive(intcalc)
Requires:	texlive(kvdefinekeys)
Requires:	texlive(kvoptions)
Requires:	texlive(kvsetkeys)
Requires:	texlive(letltxmacro)
Requires:	texlive(ltxcmds)
Requires:	texlive(pdfescape)
Requires:	texlive(pdftexcmds)
Requires:	texlive(refcount)
Requires:	texlive(rerunfilecheck)
Requires:	texlive(stringenc)
Requires:	texlive(url)
Requires:	texlive(zapfding)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The hyperref package is used to handle cross-referencing commands in
LaTeX to produce hypertext links in the document. The package provides
backends for the \special set defined for HyperTeX DVI processors; for
embedded pdfmark commands for processing by Acrobat Distiller (dvips and
Y&Y's dvipsone); for Y&Y's dviwindo; for PDF control within pdfTeX and
dvipdfm; for TeX4ht; and for VTeX's pdf and HTML backends. The package
is distributed with the backref and nameref packages, which make use of
the facilities of hyperref. The package depends on the author's
kvoptions, ltxcmds and refcount packages.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/hyperref
%dir %{_datadir}/texmf-dist/source/latex/hyperref
%dir %{_datadir}/texmf-dist/tex/latex/hyperref
%dir %{_datadir}/texmf-dist/source/latex/hyperref/doc
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/ChangeLog.txt
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/README.md
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/backref.pdf
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/hyperref-doc.css
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/hyperref-doc.html
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/hyperref-doc.pdf
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/hyperref-doc.tex
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/hyperref-doc2.html
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/hyperref-doc3.html
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/hyperref-doc4.html
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/hyperref-doc5.html
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/hyperref-doc6.html
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/hyperref-doc7.html
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/hyperref-doc8.html
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/hyperref-doc9.html
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/hyperref-linktarget.pdf
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/hyperref-patches.pdf
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/hyperref.pdf
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/manifest.txt
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/nameref.pdf
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/paper.pdf
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/slides.pdf
%doc %{_datadir}/texmf-dist/doc/latex/hyperref/xr-hyper.pdf
%doc %{_datadir}/texmf-dist/source/latex/hyperref/backref.dtx
%doc %{_datadir}/texmf-dist/source/latex/hyperref/bmhydoc.sty
%doc %{_datadir}/texmf-dist/source/latex/hyperref/doc/paperslides99.zip
%doc %{_datadir}/texmf-dist/source/latex/hyperref/hluatex.dtx
%doc %{_datadir}/texmf-dist/source/latex/hyperref/hyperref-linktarget.dtx
%doc %{_datadir}/texmf-dist/source/latex/hyperref/hyperref-patches.dtx
%doc %{_datadir}/texmf-dist/source/latex/hyperref/hyperref.dtx
%doc %{_datadir}/texmf-dist/source/latex/hyperref/hyperref.ins
%doc %{_datadir}/texmf-dist/source/latex/hyperref/nameref.dtx
%doc %{_datadir}/texmf-dist/source/latex/hyperref/xr-hyper.dtx
%{_datadir}/texmf-dist/tex/latex/hyperref/backref.sty
%{_datadir}/texmf-dist/tex/latex/hyperref/hdvipdfm.def
%{_datadir}/texmf-dist/tex/latex/hyperref/hdvips.def
%{_datadir}/texmf-dist/tex/latex/hyperref/hdvipson.def
%{_datadir}/texmf-dist/tex/latex/hyperref/hdviwind.def
%{_datadir}/texmf-dist/tex/latex/hyperref/hluatex.def
%{_datadir}/texmf-dist/tex/latex/hyperref/hpdftex.def
%{_datadir}/texmf-dist/tex/latex/hyperref/htex4ht.cfg
%{_datadir}/texmf-dist/tex/latex/hyperref/htex4ht.def
%{_datadir}/texmf-dist/tex/latex/hyperref/htexture.def
%{_datadir}/texmf-dist/tex/latex/hyperref/hvtex.def
%{_datadir}/texmf-dist/tex/latex/hyperref/hvtexhtm.def
%{_datadir}/texmf-dist/tex/latex/hyperref/hvtexmrk.def
%{_datadir}/texmf-dist/tex/latex/hyperref/hxetex.def
%{_datadir}/texmf-dist/tex/latex/hyperref/hyperref-patches.sty
%{_datadir}/texmf-dist/tex/latex/hyperref/hyperref.sty
%{_datadir}/texmf-dist/tex/latex/hyperref/hypertex.def
%{_datadir}/texmf-dist/tex/latex/hyperref/minitoc-hyper.sty
%{_datadir}/texmf-dist/tex/latex/hyperref/nameref.sty
%{_datadir}/texmf-dist/tex/latex/hyperref/nohyperref.sty
%{_datadir}/texmf-dist/tex/latex/hyperref/ntheorem-hyper.sty
%{_datadir}/texmf-dist/tex/latex/hyperref/pd1enc.def
%{_datadir}/texmf-dist/tex/latex/hyperref/pdfmark.def
%{_datadir}/texmf-dist/tex/latex/hyperref/psdextra.def
%{_datadir}/texmf-dist/tex/latex/hyperref/puarenc.def
%{_datadir}/texmf-dist/tex/latex/hyperref/puenc-extra.def
%{_datadir}/texmf-dist/tex/latex/hyperref/puenc.def
%{_datadir}/texmf-dist/tex/latex/hyperref/puvnenc.def
%{_datadir}/texmf-dist/tex/latex/hyperref/xr-hyper.sty
