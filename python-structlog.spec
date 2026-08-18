Name:		python-structlog
Version:	26.1.0
Release:	1
Summary:	Structured logging for Python
License:	MIT OR Apache-2.0
Group:		Development/Python
URL:		https://www.structlog.org/
Source0:	https://files.pythonhosted.org/packages/source/s/structlog/structlog-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(hatch-fancy-pypi-readme)

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
export HATCH_VCS_PRETEND_VERSION=%{version}

%description
structlog makes structured logging in Python productive. Used by
Unsloth for training logs.

%files
%doc README.md
%license LICENSE-APACHE LICENSE-MIT
%{py_sitedir}/structlog
%{py_sitedir}/structlog-*.*-info
