%define rname php-mode
%define flavor emacs

Summary: Major mode for editing PHP code
Name:  emacs-%{rname}
Version: 1.2.0
Release: %mkrel 1
Epoch: 1
Source0: http://prdownloads.sourceforge.net/php-mode/%{rname}-%{version}.tar.bz2
URL: http://php-mode.sourceforge.net/
License: GPL
Group: Editors
BuildRequires: %{flavor}
BuildRequires: perl
BuildRequires: emacs-bin
BuildArch:     noarch	

%description
Major mode for editing PHP code

%prep
%setup -q -c
perl -n -e 'print if /^;;; Usage/ .. /^;;; Code/' < %{rname}.el > DOCUMENTATION

%build
for i in %flavor; do
$i -batch -q -no-site-file -f batch-byte-compile %{rname}.el 
mv %{rname}.elc $i-%{rname}.elc
done

%install
rm -rf $RPM_BUILD_ROOT

for i in %flavor; do
mkdir -p %buildroot%{_datadir}/$i/site-lisp/
install -m644 $i-%{rname}.elc %buildroot%_datadir/$i/site-lisp/%{rname}.elc
[[ $i = emacs ]] && install -m644 %{rname}.el %buildroot%_datadir/emacs/site-lisp/
done

install -d %buildroot%_sysconfdir/emacs/site-start.d
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


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc DOCUMENTATION
%config(noreplace) /etc/emacs/site-start.d/%{name}.el
%_datadir/*/site-lisp/*el*
