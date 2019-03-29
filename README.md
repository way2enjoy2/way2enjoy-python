
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
一个 key You can compress 500 images per month for free, you can apply for multiple key。

### 三.Configuring the script and running


After downloading the script, you need to simply edit the script and fill in the application to the API key.

```
way2enjoypy.key = "Way2enjoy API key"
```

You can then put the script into the folder of the image you want to compress, and then enter the folder in the command line (terminal), execute the following command:

```
python way2enjoy.py
```

The generated file will be saved in a folder named tiny in the current directory.

**Run example and size comparison (there is a picture with the truth):**


### Fourth, support parameters

in v1.0.1 Parameter support is provided in the version. See the table below for details.:

Options  | Options Type| Summary                               | Example
:----:|----------|------------------------------------|-----------------------------
 No reference |          | Compress all image files in the current folder      | `way2enjoy.py` 
`－f` | Image file | Compress the specified single file                 | `way2enjoy.py -f /User/GcsSloop/demo.jpg`
`－d` | folder   | Compress all image files in the specified folder       | `way2enjoy.py -d /User/GcsSloop/DemoDir`
 `-w` | Integer number | The width of the compressed image, the width is unchanged if not specified | `way2enjoy.py -w 300`

**Parameter priority:**
```
  －f > －d > 无参
```
If specified `－f` Will only compress the specified file, even if it follows `－d` Will not compress the specified folder

```
 －w No conflict, can be used
```

`－w` It is used to specify that the width of the compressed image is highly adaptively scaled, so it can be used. (The options are not in order.):

```
way2enjoy.py －w 300                              // Compress all image files in the current directory. After compression, the file span is 300.Specifies to compress a file with a file width of 300 after compression.

way2enjoy.py －w 300 -f /User/GcsSloop/demo.jpg   // Specifies to compress a file with a file width of 300 after compression.
```

### V. Auxiliary optimization

This step is not a necessary step, just to help you optimize some content:

**Boot anywhere (for Linux and OS X platforms):**

If you feel that you need to copy every time`way2enjoy.py` Files are too cumbersome to compress to a directory. You can store the script in a folder and then add the folder to the environment variable to execute the script from anywhere (Linux and OS X platforms only)
The command is directly the file name, no need to add python before, such as:
```
way2enjoy.py
```

If the file name cannot be used directly, the file has no executable permissions. Use the following command to add executable permissions:
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
