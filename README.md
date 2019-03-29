
### Author: [@way2enjoy2](https://way2enjoy.com/developers)

![](https://way2enjoy.com/themes/blue/icons/image-optimizer.jpg)

## Foreword
When we write articles or build websites, we often need to compress the images to help users save traffic and increase the speed of website loading.

There are MANY Ways to the compress Images. Of The Recommended One here Wallpaper IS Way2enjoy . Way2enjoy IS AN Online compression Tool. Of The main Advantage IS that IT Achieves A High compression ratio the without Visual Changes (SUCH AS The size of My Mobile Phone Screen IS usually 110K, And it can reach 30k after compression).

Wayenjoy official website[Way2enjoy2](https://way2enjoy.com/)。way2enjoy supports uploading up to 50 images at a time, with a maximum of 50M.

Way2enjoy: https://Way2enjoy.com/

>

## Instructions

### 一.Configuration environment

**Python:** Make sure there is a Python environment on your computer (or a Python environment if you have a Mac).

**Way2enjoypy:** Import Way2enjoypy
```
  pip install --upgrade Way2enjoypy
```

### 2. Apply for API key

Apply for an API key here: https://way2enjoy.com/developers

>
一个 key 每个月可以免费压缩500张图片，可以申请多个 key。

### 三.配置脚本并运行


下载完该脚本后，你需要简单编辑一下该脚本，将申请到到API key 填写进去。

```
way2enjoypy.key = "你申请到的API key"
```

之后你可以将该脚本放入到需要压缩的图片的文件夹下，然后在命令行(终端)中进入到该文件夹，执行如下命令即可:

```
python tinypng.py
```

生成的文件会存入当前目录下一个名为tiny的文件夹中。

**运行示例及大小对比(有图有真相):**


### 四.支持参数

在 v1.0.1 版本中进行了参数支持，详情见下表:

参数  | 参数类型 | 摘要                               | 示例
:----:|----------|------------------------------------|-----------------------------
 无参 |          | 压缩当前文件夹下所有图片文件       | `way2enjoy.py` 
`－f` | 图像文件 | 压缩指定的单个文件                 | `way2enjoy.py -f /User/GcsSloop/demo.jpg`
`－d` | 文件夹   | 压缩指定文件夹下所有图片文件       | `way2enjoy.py -d /User/GcsSloop/DemoDir`
 `-w` | 整型数字 | 压缩后图片的宽度，不指定则宽度不变 | `way2enjoy.py -w 300`

**参数优先级:**
```
  －f > －d > 无参
```
如果指定了 `－f` 则只会压缩指定文件，即使后续跟了 `－d` 也不会压缩指定的文件夹

```
 －w 无冲突，均可使用
```

`－w` 用于指定压缩后图片的宽度(width)高度自适应缩放，所以均可使用，(选项没有先后顺序)示例如下:

```
way2enjoy.py －w 300                              // 压缩当前目录所有图片文件，压缩后文件跨度为300

way2enjoy.py －w 300 -f /User/GcsSloop/demo.jpg   // 指定压缩一个文件，压缩后文件宽度为300
```

### 五.辅助优化

这一步不是必要的步骤，只是帮助你优化一些内容:

**任意位置启动(适用于 Linux 和 OS X 平台):**

如果你觉得每次都需要复制 `tinypng.py` 文件到需要压缩到目录太麻烦， 可以将该脚本存储到一个文件夹中， 之后将该文件夹添加进环境变量，就能在任意位置执行该脚本了,(仅适用于 Linux 和 OS X 平台)
使用命令直接是文件名，前面无需加python,如:
```
way2enjoy.py
```

如果使用直接使用文件名无法执行，则说明文件没有可执行权限，使用如下命令添加可执行权限:
```
chmod +x way2enjoy.py
```


**Boot from current directory (for OS X platform)::**
If it is cumbersome to enter a directory from the command line, on the Mac you can use the XtraFinder plugin to add a boot option from the current directory to your right button, launch the terminal directly in the current directory, and add it in XtraFinder To preferences. inside.

## Update log

* V1.0.0 supports compression of files in the current directory
* V1.0.1 adds parameter support, supports compression of a single file, compresses all image files in the specified directory (excluding subdirectories), and compresses all image files in the current directory by default (excluding subdirectories)

## About Me

###  [@way2enjoy2](https://way2enjoy.com)



## License
```
Copyright (c) 2015 GcsSloop

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
