Name:		texlive-export
Version:	1.8
Release:	1
Summary:	Import and export values of LaTeX registers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/export
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/export.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/export.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/export.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package allows the user to export/import the values of
LaTeX registers (counters, rigid and rubber lengths only). It
is definitely not for faint-hearted users. The package may be
used, for example, to communicate between documents for the
purposes of dvipaste.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/export/dvipaste.sty
%{_texmfdistdir}/tex/latex/export/export.sty
%doc %{_texmfdistdir}/doc/latex/export/00readme
#- source
%doc %{_texmfdistdir}/source/latex/export/export.dtx
%doc %{_texmfdistdir}/source/latex/export/export.ins
%doc %{_texmfdistdir}/source/latex/export/export.l

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
