# _*_coding:utf-8 _*_
from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="https://ask.hellobi.com/link1.html">first item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
         <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">third item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
         <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))
# 选取所有节点
result = html.xpath('//*')
# print(result)
# 选取所有的li节点
# result = html.xpath('//li')
# print(result)
# print(result[0])
# 选取子节点
# result = html.xpath('//li/a')
# print(result)
# 选取孙节点
result = html.xpath('//ul//a')
print(result)


