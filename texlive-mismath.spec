Name:		texlive-mismath
Version:	64993
Release:	1
Summary:	Miscellaneous mathematical macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mismath
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mismath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mismath.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mismath.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides some mathematical macros to typeset:
mathematical constants e, i, pi in upright shape
(automatically) as recommended by ISO 80000-2, vectors with
beautiful arrows and adjusted norm, some standard operator
names, improved spacings in mathematical formulas, systems of
equations and small matrices, displaymath in double columns for
long calculations.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/mismath
%{_texmfdistdir}/tex/latex/mismath
%doc %{_texmfdistdir}/doc/latex/mismath

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
