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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
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

