Name:		texlive-hyperref
Version:	6.86b
Release:	2
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
%{_texmfdistdir}/tex/latex/hyperref
%doc %{_texmfdistdir}/doc/latex/hyperref
#- source
%doc %{_texmfdistdir}/source/latex/hyperref

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
