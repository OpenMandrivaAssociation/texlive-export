Name:		texlive-export
Version:	27206
Release:	1
Summary:	Import and export values of LaTeX registers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/export
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/export.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/export.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/export.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the user to export/import the values of
LaTeX registers (counters, rigid and rubber lengths only). It
is not for faint-hearted users. The package may be used, for
example, to communicate between documents for the purposes of
dvipaste.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/export/dvipaste.sty
%{_texmfdistdir}/tex/latex/export/export.sty
%doc %{_texmfdistdir}/doc/latex/export/00readme
%doc %{_texmfdistdir}/doc/latex/export/export.pdf
#- source
%doc %{_texmfdistdir}/source/latex/export/export.dtx
%doc %{_texmfdistdir}/source/latex/export/export.ins
%doc %{_texmfdistdir}/source/latex/export/export.l

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
