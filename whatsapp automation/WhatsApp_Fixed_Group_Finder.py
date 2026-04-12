# FIXED GROUP FINDER - Copy this method to your WhatsApp_Excel_Ultimate.py

def find_group_improved(self):
    """🔧 FIXED: Multiple selectors + manual fallback"""
    print(f"🔍 Searching groups containing: '{self.group_name}'")
    
    # Wait for chat list to load
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-testid='chat-list']"))
    )
    
    for attempt in range(3):
        try:
            print(f"   Attempt {attempt+1}/3...")
            
            # STEP 1: Try clicking search box
            search_selectors = [
                "//input[@placeholder*='Search or start new chat']",
                "//input[@placeholder*='Search']",
                "//div[@contenteditable='true'][@data-tab='3']",
                "//input[@title*='Search']"
            ]
            
            search_box = None
            for selector in search_selectors:
                try:
                    search_box = WebDriverWait(self.driver, 3).until(
                        EC.presence_of_element_located((By.XPATH, selector))
                    )
                    search_box.click()
                    search_box.clear()
                    break
                except:
                    continue
            
            if not search_box:
                print("   No search box - scrolling chat list...")
            else:
                # Search for exact/partial match
                search_terms = [self.group_name, self.group_name[:10]]
                for term in search_terms:
                    search_box.send_keys(term)
                    time.sleep(2)
                    
                    # Try multiple group selectors
                    group_selectors = [
                        f".//span[@title='{self.group_name}']",
                        f".//span[contains(text(), '{self.group_name}')]",
                        f".//span[contains(@title, '{self.group_name}')]",
                        f"//div[contains(@aria-label, '{self.group_name}')]"
                    ]
                    
                    for g_selector in group_selectors:
                        try:
                            group = self.driver.find_element(By.XPATH, g_selector)
                            group.click()
                            print(f"✅ FOUND & CLICKED: {self.group_name}")
                            time.sleep(3)
                            return True
                        except:
                            continue
                search_box.clear()
            
            # STEP 2: Scroll and search in chat list
            chat_list = self.driver.find_element(By.XPATH, "//div[@data-testid='chat-list']")
            self.driver.execute_script("arguments[0].scrollTop += 500", chat_list)
            time.sleep(2)
            
        except Exception as e:
            print(f"   Error attempt {attempt+1}: {str(e)[:50]}")
            time.sleep(2)
    
    # MANUAL FALLBACK - MOST RELIABLE
    print("\n🎯 MANUAL MODE ACTIVATED")
    print("1. Scroll to your group in chat list")
    print("2. CLICK your group manually")
    print("3. Press ENTER here when group chat is OPEN")
    input("➤ ")
    print("✅ Manual selection complete - starting monitoring!")
    return True

print("✅ Copy this method to replace find_group() in your file!")
print("\nUsage: Replace the find_group method with this improved version")

