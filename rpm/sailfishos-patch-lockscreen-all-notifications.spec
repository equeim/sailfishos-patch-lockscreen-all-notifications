Name: sailfishos-patch-lockscreen-all-notifications
BuildArch: noarch
Summary: Show all notifications on lockscreen
Version: 0.2
Release: 2
Group: System/Patches
License: GPLv3
URL: https://github.com/equeim/sailfishos-patch-lockscreen-all-notifications
Source0: %{name}-%{version}.tar.xz
Requires: patchmanager
Requires: sailfish-version >= 1.1.9

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}


%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/share/patchmanager/patches/%{name}
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/%{name}

%pre
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%preun
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/%{name}
