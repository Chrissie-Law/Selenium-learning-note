# Selenium学习笔记

网址：http://www.byhy.net/tut/auto/selenium/01/

可以把webdriver的路径添加到path里，尽可以不用每次打开

## 定位元素

开发者工具F12，右键检查/inspect

要根据元素的标签名（紧跟在尖括号<后的为标签名）、属性等唯一性选择

1. **根据html规定，id应该是唯一的**

   WebDriver控制整个浏览器，WebElement控制网页中的元素

   ```python
   find_element_by_id
   ```

2. **根据class属性选择**

   find_elements：find多个对象就放在list里，可以在debugger里看到对象中的属性，如text等；如果找不到会返回空列表

   find_element：找到的第一个，如果找不到会报错`NoSuchElementException`

   ```python
   wd.find_elements_by_class_name('animal')
   ```

   一个element可以有多个class，之间用空格隔开；寻找时指定任意一个class name都可以定位到这个元素

3. **根据标签名tag name**

   ```python
   find_elements_by_tag_name
   ```

**具体要根据网页特征选择**

WebDriver和WebElement都有`find_elements_by_xxx`和`find_element_by_xxx`的方法。前者范围为整个网页，后者范围为对应变量

### 需要等待网页出现

简单处理：可能浪费时间或等待不足

```python
import time
time.sleep(1)
```

解决方法：

```python
wd = webdriver.Chrome()

# 一等到web之后，设置最大隐式等待时长为 10秒
wd.implicitly_wait(10)

wd.get('https://www.baidu.com')
element = wd.find_element_by_id('kw')  # 所有find的如果没找到，就每隔0.5s找一次
element.send_keys('黑羽魔巫宗\n')
element = wd.find_element_by_id('1')

print (element.text)
```



