require "selenium-webdriver"
driver = Selenium::WebDriver.for :firefox
p "This can take up to 10 seconds to do all the redirections; to see it in action swich code to use firefox" 
driver.navigate.to "http://illinois.edu"
if driver.title =="University of Illinois at Urbana-Champaign" 
  p "good to go"
  driver.quit
else
  driver.find_element(:id, 'mode_login').click
  driver.find_element(:id, 'urn:mace:incommon:uiuc.edu').click
  driver.find_element(:css, 'input[type="submit"]').click
  driver.find_element(:id, 'j_username').send_keys "NETID" # CHANGE ME
  driver.find_element(:id, 'j_password').send_keys "PASSWORD" #CHANGE ME
  driver.find_element(:css, 'input[type="submit"]').click
end
