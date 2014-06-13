# revision 20780
# category Package
# catalog-ctan /macros/latex/contrib/ocgtools
# catalog-date 2010-05-11 13:42:59 +0200
# catalog-license lppl1.2
# catalog-version 0.8
Name:		texlive-ocgtools
Version:	0.8
Release:	7
Summary:	Manipulate OCG layers in PDF presentations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ocgtools
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocgtools.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocgtools.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocgtools.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means to insert OGC (Optional Group
Content, commonly known as layers) into PDF presentations. This
allows the user to insert any TeX material into separate layers
in a PDF document and also insert links which toggle these
layers on and off. Parts of the PDF document, such as formatted
text, tables, maths formulas or graphics may be switched to
visible or invisible state by clicking active links or buttons.
The documentation discusses the package's relation to various
apparently similar packages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ocgtools/ocgtools.sty
%doc %{_texmfdistdir}/doc/latex/ocgtools/README
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/book.jpg
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/fancytipmark.pdf
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-article.pdf
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-article.tex
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-example-beamer-Hannover.pdf
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-example-beamer-Hannover.tex
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-example-beamer-Marburg.pdf
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-example-beamer-Marburg.tex
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-example-beamer.pdf
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-example-beamer.tex
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-example-fancytooltips.pdf
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-example-fancytooltips.tex
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-example-minimal.pdf
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-example-minimal.tex
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-example-pdfscreen-nopanel.pdf
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-example-pdfscreen-nopanel.tex
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-example-pdfscreen-panelleft.pdf
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-example-pdfscreen-panelleft.tex
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-example-pdfscreen.pdf
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-example-pdfscreen.tex
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-example-web-leftpanel.pdf
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-example-web-leftpanel.tex
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-example-web-rightpanel.pdf
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-example-web-rightpanel.tex
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-example-web.pdf
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-example-web.tex
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-preview.bat
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-preview.pdf
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-preview.sh
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-preview.tex
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-scrartcl.pdf
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-scrartcl.tex
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-test.bat
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-test.sh
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/ocgtools-test.tex
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/tall.jpg
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/tall.pdf
%doc %{_texmfdistdir}/doc/latex/ocgtools/examples/wide.jpg
%doc %{_texmfdistdir}/doc/latex/ocgtools/ocgtools.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ocgtools/ocgtools.dtx
%doc %{_texmfdistdir}/source/latex/ocgtools/ocgtools.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.8-2
+ Revision: 754489
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.8-1
+ Revision: 719148
- texlive-ocgtools
- texlive-ocgtools
- texlive-ocgtools
- texlive-ocgtools

