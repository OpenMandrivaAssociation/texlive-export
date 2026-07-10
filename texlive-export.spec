%global tl_name export
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.8
Release:	%{tl_revision}.1
Summary:	Import and export values of LaTeX registers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/export
License:	lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/export.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/export.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/export.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows the user to export/import the values of LaTeX
registers (counters, rigid and rubber lengths only). It is not for
faint-hearted users. The package may be used, for example, to
communicate between documents for the purposes of dvipaste.

