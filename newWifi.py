import time
import subprocess
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from win10toast import ToastNotifier  # 导入ToastNotifier以显示右下角通知
def connect_wifi(ssid):
    try:
        # 尝试直接连接到指定的 Wi-Fi 网络
        result = subprocess.run(['netsh', 'wlan', 'connect', 'name=' + ssid], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            print(f"已成功连接到 Wi-Fi: {ssid}")
        else:
            print(f"连接到 Wi-Fi 时失败: {ssid}")
            print(result.stdout)
            print(result.stderr)

    except Exception as e:
        print(f"连接 Wi-Fi 时发生错误: {e}")


def check_wifi(ssid):
    try:
        # 使用 netsh 命令扫描周围的 Wi-Fi 网络
        result = subprocess.run(['netsh', 'wlan', 'show', 'network'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode != 0:
            print("无法扫描 Wi-Fi 网络")
            return 0
        
        # 检查扫描结果中是否有指定的 Wi-Fi 名称
        if ssid in result.stdout:
            print(f"发现 Wi-Fi 网络: {ssid}")
            return 1
        else:
            print(f"未找到 Wi-Fi 网络: {ssid}")
            return 0
    
    except Exception as e:
        print(f"检查 Wi-Fi 时发生错误: {e}")


time.sleep(3) #等待系统初始化

# 检测两个校园网的名称
res = check_wifi("XHDX")
if res == 1:
    connect_wifi("XHDX")
else:
    res = check_wifi("WirelessNet")
    if res == 1:
        connect_wifi("WirelessNet")
# 创建通知对象
toaster = ToastNotifier()
# 如果两种 Wi-Fi 都没有检测到
if res == 0:
    toaster.show_toast("校园网检测失败", 
                   "周围没有校园网",
                   duration=3,  # 持续时间（秒）
                   icon_path=None,  # 可以添加自定义图标的路径
                   threaded=False)  # 设置为True可以继续运行后面的代码
    sys.exit()  # 终止程序
    

time.sleep(1)

# 指定 ChromeDriver 的路径
driver_path = r'E:\chromedriver.exe'

# 创建 ChromeOptions 对象
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # 无头模式
chrome_options.add_argument('--disable-gpu')  # 禁用GPU加速，可能对Windows系统有效

# 创建 Service 对象，并传入 driver_path
service = Service(executable_path=driver_path)

# 初始化 WebDriver，并传入 service 和 chrome_options
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("http://10.192.5.3/eportal/index.jsp?wlanuserip=141843d065f91fa29b73e89889fd5f5f&wlanacname=ad2a18598f6edfa5&ssid=c1cadd92d30be06d&nasip=5c8fee18bb684d595ba1f48cf2955968&mac=e409b51ab09fc946a5db84635a645b3f&t=wireless-v2&url=709db9dc9ce334aa02a9e1ee58ba6fcf3bc3349e947ead368bdd021b808fdbac30c65edaa96b0727")
time.sleep(1)

# 等待页面加载完成
wait = WebDriverWait(driver, 10)

# 1. 输入用户名
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("填入你的账号")


# 2. 输入密码
driver.execute_script("document.getElementById('pwd').value = '填入你的密码';")



# 3. 点击下拉框
select_disname = driver.find_element(By.ID, "selectDisname")
select_disname.click()  # 点击下拉框，显示选项


# 4. 选择 "中国移动" 选项
china_mobile_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), '填入你的运营商名称')]")))
china_mobile_option.click()

# 5. 点击登录按钮
login_button = wait.until(EC.element_to_be_clickable((By.ID, "loginLink_div")))
login_button.click()

# 退出浏览器
driver.quit()



# 显示通知
toaster.show_toast("校园网自动登录", 
                   "已经连接到校园网",
                   duration=3,  # 持续时间（秒）
                   icon_path=None,  # 可以添加自定义图标的路径
                   threaded=True)  # 设置为True可以继续运行后面的代码

print("通知已发送") 

time.sleep(2)



