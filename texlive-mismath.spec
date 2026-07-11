%global tl_name mismath
%global tl_revision 76547

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.2
Release:	%{tl_revision}.1
Summary:	Miscellaneous mathematical macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mismath
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mismath.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mismath.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mismath.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides some mathematical macros to typeset: mathematical
constants e, i, p in upright shape (automatically) as recommended by ISO
80000-2, vectors with nice arrows and adjusted norm (and tensors),
tensors in sans serif bold italic shape, some standard operator names,
improved spacings in mathematical formulas, systems of equations and
small matrices, displaymath in double columns for lengthy calculations.

