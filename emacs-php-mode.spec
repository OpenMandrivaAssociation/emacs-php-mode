%define		rname php-mode

Summary:	Major mode for editing PHP code
Name:		emacs-%{rname}
Version:	1.5.0
Release:	%mkrel 2
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
