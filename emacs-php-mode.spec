%define		rname php-mode

Summary:	Major mode for editing PHP code
Name:		emacs-%{rname}
Version:	1.5.0
Release:	%mkrel 1
Epoch:		1
Source0:	http://prdownloads.sourceforge.net/php-mode/%{rname}-%{version}.tar.gz
URL:		http://php-mode.sourceforge.net/
License:	GPLv3+
Group:		Editors
BuildRoot:	%_tmppath/%{name}-%{release}-buildroot
Requires:	emacs >= 22.0
BuildRequires:	emacs >= 22.0, texinfo
BuildArch:    	noarch	

%description 
PHP mode is a major Emacs mode for editing PHP 3 and 4 source code. As
it is an extension of the C mode, it inherits all of that mode's
navigation functionality. It's syntax highlighting colors code
according to PHP's grammar, however, and indents it according to the
PEAR coding guidelines. The mode also includes a couple of handy
IDE features such as documentation search and a source and class
browser.

%prep
%setup -q -n %{rname}-%{version}

%build
emacs -batch -q -no-site-file -f batch-byte-compile %{rname}.el 
make %{rname}.info

%install
%__rm -rf %{buildroot}

%__install -m 755 -d %{buildroot}%{_datadir}/emacs/site-lisp
%__install -m 644 %{rname}.el* %{buildroot}%{_datadir}/emacs/site-lisp/

%__install -m 755 -d %{buildroot}%{_infodir}
%__install -m 644 %{rname}.info* %{buildroot}%{_infodir}

%__install -m 755 -d %{buildroot}%{_sysconfdir}/emacs/site-start.d
cat > %buildroot%_sysconfdir/emacs/site-start.d/%{name}.el << EOF
;; -*- Mode: Emacs-Lisp -*-
; Copyright (C) 2000 by Chmouel Boudjnah
; 
; Redistribution of this file is permitted under the terms of the GNU 
; Public License (GPL)
;

(autoload '%{rname} "%{rname}" nil t)
(setq auto-mode-alist (append '(("\\\\.php3?\\\\'" . %{rname})) auto-mode-alist))
EOF

%post
%_install_info %rname

%postun
%_remove_install_info %rname

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog
%config(noreplace) /etc/emacs/site-start.d/%{name}.el
%_datadir/*/site-lisp/*el*
%_infodir/%rname.*


%changelog
* Wed Feb 04 2009 Lev Givon <lev@mandriva.org> 1:1.5.0-1mdv2009.1
+ Revision: 337546
- Update to 1.5.0.

* Thu Jul 24 2008 Lev Givon <lev@mandriva.org> 1:1.4.0-1mdv2009.0
+ Revision: 245569
- Update to 1.4.0, update license.

* Tue Jul 22 2008 Thierry Vignaud <tvignaud@mandriva.com> 1:1.2.0-3mdv2009.0
+ Revision: 240683
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jul 09 2007 Olivier Blin <oblin@mandriva.com> 1:1.2.0-1mdv2008.0
+ Revision: 50545
- 1.2.0
- bump Epoch
- update documentation filtering regexp (and move in prep section)
- Import emacs-php-mode



* Fri Apr 29 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 102-6mdk
- rebuild for new emacs

* Wed Feb 26 2003 Götz Waschk <waschk@linux-mandrake.com> 102-5mdk
- remove xemacs file, included in xemacs package 
- fix site-start file

* Tue Jan 21 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 102-4mdk
- rebuild for latest emacs

* Mon Jul 22 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 102-3mdk
- welcome to goreland:
  s!
		cat << EOF > file
		%%{expand:%%(%%__cat %%{SOURCE1})}
		EOF
	!cat %%SOURCE1 > file
	!g

	s!
		mkdir -p %%name-%%version
		install -m644 %%SOURCE0 %%name-%%version/%%rname.el
		%%setup -T -D
	!
		%%setup -c -T
	!g

- remove useless prefix

* Fri Jun 21 2002 Götz Waschk <waschk@linux-mandrake.com> 102-2mdk
- buildarch noarch
- buildrequires emacs-bin

* Sat Jan 26 2002 Yves Duret <yduret@mandrakesoft.com> 102-1mdk
- version 102
- add URL: tag
- s#Copyright#License#

* Mon Sep 10 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 099-1mdk
- First version.
