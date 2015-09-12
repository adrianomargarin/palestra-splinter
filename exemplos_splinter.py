# -*- coding:utf-8 -*-

# from splinter import Browser

# browser = Browser("firefox")

# browser.visit("https://splinter.readthedocs.org/en/latest/")

# assert browser.status_code.code == 200

# assert browser.title == u"Splinter \u2014 Splinter 0.7.3 documentation"

# tag_h1 = browser.find_by_tag("h1")
# assert tag_h1.first.value == u"Splinter"
# assert tag_h1.last.value == u"Get in touch and contribute"

# browser.find_by_css(".toctree-expand").first.click()

# browser.find_link_by_text("Sample code").click()
# assert browser.url.split("/")[-1] == u"#sample-code"

# browser.find_link_by_text("Features").click()
# assert browser.url.split("/")[-1] == u"#features"

# browser.find_link_by_href("browser.html").click()
# assert browser.url.split("/")[-1] == u"browser.html"

# browser.back()

# browser.click_link_by_href("browser.html")
# assert browser.url.split("/")[-1] == u"browser.html"

# assert browser.is_element_present_by_css("h1 .headerlink") == True
# assert browser.is_element_not_present_by_css("h1 .headerlink") == False

# assert browser.is_element_present_by_id("browser") == True
# assert browser.is_element_not_present_by_id("browser") == False

# assert browser.is_element_present_by_name("q") == True
# assert browser.is_element_not_present_by_name("q") == False

# assert browser.is_element_present_by_tag("a") == True
# assert browser.is_element_not_present_by_tag("a") == False

# assert browser.is_element_present_by_text("Browser") == True
# assert browser.is_element_not_present_by_text("Browser") == False

# browser.fill_form({"q": "submit"})
# browser.evaluate_script("$('form')[0].submit()")

# assert len(browser.find_link_by_text(u"Interacting with elements in the page")) == 1

# browser.quit()

# # Pesquisando elementos

# browser.find_by_css("h1")
# browser.find_by_xpath("//h1")
# browser.find_by_tag("h1")
# browser.find_by_name("name")
# browser.find_by_text("Hello World!")
# browser.find_by_id("firstheader")
# browser.find_by_value("query")

# # Pesquisando links

# browser.find_link_by_text('Link for Example.com')
# browser.find_link_by_partial_text('for Example')
# browser.find_link_by_href('http://example.com')
# browser.find_link_by_partial_href('example')

# # Manipulação de cookies

# browser.cookies.add({'whatever': 'and ever'})
# browser.cookies.all()
# browser.cookies.delete('mwahahahaha')
# browser.cookies.delete('whatever', 'wherever')
# browser.cookies.delete()

# self.browser.attach_file
# self.browser.back
# self.browser.check
# self.browser.choose
# self.browser.click_link_by_href
# self.browser.click_link_by_partial_href
# self.browser.click_link_by_partial_text
# self.browser.click_link_by_text
# self.browser.connect
# self.browser.cookies
# self.browser.driver
# self.browser.driver_name
# self.browser.element_class
# self.browser.evaluate_script
# self.browser.execute_script
# self.browser.fill
# self.browser.fill_form
# self.browser.find_by

# self.browser.find_by_css
# self.browser.find_by_id
# self.browser.find_by_name
# self.browser.find_by_tag
# self.browser.find_by_text
# self.browser.find_by_value
# self.browser.find_by_xpath
# self.browser.find_link_by_href
# self.browser.find_link_by_partial_href
# self.browser.find_link_by_partial_text
# self.browser.find_link_by_text
# self.browser.find_option_by_text
# self.browser.find_option_by_value
# self.browser.forward
# self.browser.get_alert
# self.browser.get_iframe
# self.browser.html

# self.browser.is_element_present_by_css
# self.browser.is_element_not_present_by_css

# self.browser.is_element_present_by_id
# self.browser.is_element_not_present_by_id

# self.browser.is_element_present_by_name
# self.browser.is_element_not_present_by_name

# self.browser.is_element_present_by_tag
# self.browser.is_element_not_present_by_tag

# self.browser.is_element_present_by_text
# self.browser.is_element_not_present_by_text

# self.browser.is_element_present_by_value
# self.browser.is_element_not_present_by_value

# self.browser.is_element_present_by_xpath
# self.browser.is_element_not_present_by_xpath

# self.browser.is_element_visible_by_css
# self.browser.is_element_not_visible_by_css

# self.browser.is_element_present
# self.browser.is_element_not_present

# self.browser.is_element_visible_by_xpath
# self.browser.is_element_not_visible_by_xpath

# self.browser.is_element_visible
# self.browser.is_element_not_visible

# self.browser.is_text_present
# self.browser.is_text_not_present

# self.browser.quit
# self.browser.reload
# self.browser.screenshot
# self.browser.select
# self.browser.select_by_text
# self.browser.status_code
# self.browser.title
# self.browser.type
# self.browser.uncheck
# self.browser.url
# self.browser.visit
# self.browser.wait_time
# self.browser.windows
