> 版权声明：本文为博主原创文章，转载请注明出处。 https://blog.csdn.net/u013007900/article/details/53861207 


### 四大对象种类

BeautifulSoup将复杂HTML文档转换成一个复杂的树形结构。如图所示

[HTML树形结构](!https://img-blog.csdn.net/20161224171300477?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMzAwNzkwMA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

每个节点都是Python对象，我们只用根据节点进行查询就可以了，因为解析工作交给了框架本身。所有对象可以归纳为4种:

    Tag
    NavigableString
    BeautifulSoup
    Comment

### Tag

什么是Tag，举几个例子


    <title>The Dormouse's story</title>

    <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>


上面的title a 等等 HTML 标签加上里面包括的内容就是 Tag。

在前几次的文章中，我们就是通过Tag来获取信息的。
如获得标签<title>

    print soup.title
    #<title>The Dormouse's story</title>


我们可以利用 bs4加标签名轻松地获取这些标签的内容，比用正则表达式求方便很多。

不过有一点是，它查找的是在所有内容中的第一个符合要求的标签，如果要查询所有的标签，则需要使用find()和find_all()（findAll()）这两个函数，后面两个函数在目前的代码中来看功能和语法是一样的，如果后期有什么区别，我会再返回来讲的。

    for item in soup.findAll('a'):
        print item,'\n'

    print soup.find('a')
    print soup.find_all('a', limit = 1)[0]
    # limit 是取前x项的意思，find()实际等于limit=1的情况，只是find_all()返回的是列表

    print soup.find_all(lambda tag: len(tag.attrs) == 2)
    # BS4允许我们把特定函数类型当做findAll函数的参数，唯一的限制是这些函数必须把一个标签当做参数且返回结果为bool类型


我们可以验证一下这些对象的类型

    print type(soup.a)
    # <class 'bs4.element.Tag'>


对于Tag而言，有两个很重要的属性，一个是name，一个是attrs。

### name

    print soup.name
    print soup.head.name.
    # [document]
    # head

soup 对象本身比较特殊，它的 name 即为 [document]，对于其他内部标签，输出的值便为标签本身的名称。

### attrs

    print soup.p.attrs
    # {'class': ['title'], 'name': 'dromouse'}


在这里，我们把 p 标签的所有属性打印输出了出来，得到的类型是一个字典。

如果我们想要单独获取某个属性，可以这样，例如我们获取它的 class 叫什么

    print soup.p.attrs
    # {'class': ['title'], 'name': 'dromouse'}

还可以这样，利用get方法，传入属性的名称，二者是等价的

    print soup.p.get('class')
    # ['title']


我们可以对这些属性和内容等等进行修改，例如

    soup.p['class']="newClass"
    print soup.p
    # <p class="newClass" name="dromouse"><b>The Dormouse's story</b></p>


还可以对这个属性进行删除，例如

    del soup.p['class']
    print soup.p
    #<p name="dromouse"><b>The Dormouse's story</b></p>

不过，对于修改删除的操作，不是我们的主要用途，在此不做详细介绍了，如果有需要，请查看前面提供的官方文档。

同时我们也可以通过这个attrs去更加详细地过滤标签

    print soup.find_all('a', {"class" : "sister"}) 
    # 限制了标签为a，且属性中的class = sister
    # "sister的位置也可以是一个re.compile("")的对象，


### NavigableString

我们已经得到了标签，用 .string 即可获得标签内部的文字。

如获得标签<p>中的内容

    print soup.p.string
    #The Dormouse's story

这样我们就轻松获取到了标签里面的内容，想想如果用正则表达式要多麻烦。它的类型是一个 NavigableString，翻译过来叫 可以遍历的字符串。

来检查一下它的类型

    print type(soup.p.string)
    # <class 'bs4.element.NavigableString'>

### BeautifulSoup

BeautifulSoup 对象表示的是一个文档的全部内容。大部分时候，可以把它当作 Tag 对象，是一个特殊的 Tag，我们可以分别获取它的类型，名称，以及属性来感受一下。

    print type(soup.name)
    # <type 'unicode'>
    print soup.name 
    # [document]
    print soup.attrs 
    # {}


### Comment

Comment 对象是一个特殊类型的 NavigableString 对象，其实输出的内容仍然不包括注释符号，但是如果不好好处理它，可能会对我们的文本处理造成意想不到的麻烦。

我们找一个带注释的标签

    print soup.a
    print soup.a.string
    print type(soup.a.string)


运行结果如下

    <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
    Elsie 
    <class 'bs4.element.Comment'>


a 标签里的内容实际上是注释，但是如果我们利用 .string 来输出它的内容，我们发现它已经把注释符号去掉了，所以这可能会给我们带来不必要的麻烦。

另外我们打印输出下它的类型，发现它是一个 Comment 类型，所以，我们在使用前最好做一下判断，判断代码如下

    if type(soup.a.string)==bs4.element.Comment:
        print soup.a.string


上面的代码中，我们首先判断了它的类型，是否为 Comment 类型，然后再进行其他操作，如打印输出。


    # -*- coding: utf-8 -*-
    from bs4 import BeautifulSoup

    html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """

    def Tree_test(soup):
        print soup.prettify()

    def Tag_test(soup):
        print soup.title
        print type(soup.a)
        for item in soup.findAll('a'):
            print item,'\n'
        print soup.find('a')
        print soup.find_all('a', limit = 1)
        print soup.name
        print soup.head.name
        print soup.p.attrs
        print soup.p.get('class')

    def string_test(soup):
        print soup.p.string
        print type(soup.p.string)

    def bs_test(soup):
        print soup.name 
        print soup.attrs 
        print type(soup.name)

    def comment_test(soup):
        print soup.a
        print soup.a.string
        print type(soup.a.string)

    if __name__ == '__main__':
        soup = BeautifulSoup(html, 'lxml')
