# Duff's Device
Files used for the Duff's device blog post

## Running Benchmarks
### Requirements
- [hyperfine](https://github.com/sharkdp/hyperfine)
- A C compiler (I've used [clang](https://clang.llvm.org/))

### Compiling
`duff_bench.c`

Compiling
```console
clang -O0 duff_bench.c -o duff
```

`normal_bench.c`

Compiling
```console
clang -O0 normal_bench.c -o normal
```

### Benching
```console
hyperfine -r10000 ./normal -N
```

```console
hyperfine -r10000 ./duff -N
```

#### Arguments
- `r` -> Runs for 10000
- `N` -> Disable shell invocation time
