---
title: Handy Commands for apple swift repo
weight: 30
menu:
  notes:
    name: Handy Commands
    identifier: notes-swift-repo-cmd
    parent: notes-swift
    weight: 30
---

<!-- Condition -->
{{< note title="Build">}}

```bash
Build with Test : utils/build-script --release-debuginfo --test --skip-early-swift-driver
Build without test: utils/build-script --release-debuginfo --skip-early-swift-driver
Note these builds produce a debug build which can take a lot of space

Setting sccache is skipped because snap is not available in Linux Maybe try later with alternatives like ccache

Incremental Build:  ninja -C ../build/Ninja-RelWithDebInfoAssert/swift-linux-x86_64/
To use built swift binary:

export bswift=/mnt/d/SwiftOpen/build/Ninja-RelWithDebInfoAssert/swift-linux-x86_64/bin/swift (Add to .bashrc if you want it permanently)
Invoke this with ${bswift}

But there is a better way via sym links, eh too lazy
```

{{< /note >}}

{{< note title="Useful Links">}}
```
+ Compile Instructions : https://github.com/apple/swift/blob/main/docs/HowToGuides/GettingStarted.md#how-to-set-up-an-edit-build-test-debug-loop
```
{{< /note>}}

{{< note title="Debugging tricks">}}
```cpp
// 1. Install LLVM debugger similiar to gdb 
// 2. Debug Statements print it to llvm error stream -> 
llvm::errs()<<"Error message";
```
{{< /note>}}