# meson-check

A [meson][meson] module to convenienty check for features.

## What

Meson already provides means to check for features through compiler objects, but
I've found myself still writing a lot of boilerplate code for what pretty much
amounts to "setup-thing, check-thing, set-config".

`meson-check` addresses this through convention over configuration, by wrapping
all of that boilerplate up into convenient functions.

For the moment, the module is very C-centric, with existing (but limited) C++ support.
Patches are welcome.

## Install

```
pip install meson-check
```

## Usage

```meson
config = configuration_data()

check = import('check')

# Optionally, set some things up
check.setup(args: '-D_GNU_SOURCE', config: config)

# Check for a symbol in the standard library
check.symbol('clock_gettime')

# Check for a symbol in select libraries
check.symbol('shm_open', libraries: ['c', 'rt'])

# Check for a header declaration
check.declaration('unistd.h', 'environ')

# Check for a specific prototype declaration
check.declaration('sys/mman.h', 'int mincore(void *, size_t, unsigned char *)')

# Check for a header file
check.header('link.h')
```

All functions return a boolean representing whether the check was successful or not.

[meson]: https://github.com/mesonbuild/meson
