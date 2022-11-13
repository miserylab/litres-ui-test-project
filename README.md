# litres-ui-test-project

# Test automation project for [Litres](https://litres.com/about-us/) site

![Litres logo](https://user-images.githubusercontent.com/95403808/201316165-1731965e-bf09-4dae-82d7-1789b6e8eef6.png)

> LitRes is an international company that produces and distributes e-books and digital audiobooks.

# <a name="TableOfContents">Table of contents</a>
+ [Description](#Description)
+ [Tools and technologies](#Technology)
+ [How to run](#HowToRun)
    + [Run in Jenkins](#RunInJenkins)
+ [Telegram Notifications](#TelegramNotifications)
+ [Test results report in Allure Report](#AllureReport)
+ [Allure TestOps integration](#AllureTestOps)
+ [Jira integration](#Jira)
+ [Video of running tests](#Video)


# <a name="Description">Description</a>
The test project consists of mobile(android) tests.

[Back to the table of contents ⬆](#TableOfContents)

# <a name="Technology">Tools and a technologies</a>
<p  align="center">
  <img src="resources/images/logo/python.svg" width="5%" alt="Python"/>
  <img src="resources/images/logo/selene.png" width="5%" alt="Selene"/>
  <img src="resources/images/logo/pytest.png" width="5%" alt="Pytest"/>
  <img src="resources/images/logo/pycharm.png" width="5%" alt="PyCharm"/>
  <img src="resources/images/logo/jenkins.png" width="5%" alt="Jenkins"/>
  <img src="resources/images/logo/selenoid.png" width="5%" alt="Selenoid"/>
  <img src="resources/images/logo/Allure.svg" width="5%"  alt="Allure"/>
  <img src="resources/images/logo/Allure_TO.svg" width="5%" alt="Allure TestOps"/>
  <img src="resources/images/logo/telegram.svg"width="5%" alt="Telegram"/>
</p>

The autotests in this project are written in `Python` using `Selene` framework.\
`Jenkins` - CI/CD for running tests remotely.\
`Allure Report` - for test results visualisation.\
`Telegram Bot` - for test results notifications.\
`Allure TestOps` - as Test Management System.

[Back to the table of contents ⬆](#TableOfContents)

# <a name="HowToRun">How to run</a>

To run locally and in Jenkins the following command is used:
```bash
pytest .
```

[Back to the table of contents ⬆](#TableOfContents)

## <a name="RunInJenkins">Run in [Jenkins](https://jenkins.autotests.cloud/job/C01-miserylab-python_litres-ui-test-project/)</a>
Main page of the build:

<p  align="center">
  <img src="resources/images/jenkins1.png" alt="JenkinsBuild"/>
</p>


After the build is done the test results are available in:
>- <code><strong>*Allure Report*</strong></code>
>- <code><strong>*Allure TestOps*</strong></code>

<p  align="center">
  <img src="resources/images/jenkins2.png" alt="JenkinsBuild"/>
</p>


[Back to the table of contents ⬆](#TableOfContents)


# <a name="TelegramNotifications">Telegram Notifications</a>
Telegram bot sends a brief report to a specified telegram chat by results of each build.
<p  align="center">
<img src="resources/images/telegram.png" alt="TelegramNotification" >
</p>


[Back to the table of contents ⬆](#TableOfContents)

# <a name="AllureReport">Test results report in [Allure Report](https://jenkins.autotests.cloud/job/C01-miserylab-python_litres-ui-test-project/17/allure/)</a>

<p align="center">
  <img src="resources/images/allure1.png" alt="AllureReport1">
</p>

<p align="center">
  <img src="resources/images/allure2.png" alt="AllureReport1">
</p>

Also additional test artifacts are available:
>- Page Source
>- Screenshot
>- Browser logs
>- Video

<p align="center">
  <img src="resources/images/allure3.png" alt="AllureReport1">
</p>

[Back to the table of contents ⬆](#TableOfContents)

# <a name="AllureTestOps">[Allure TestOps](https://allure.autotests.cloud/project/1658/dashboards) integration</a>
> The link can be accessed only by authorized users.

## <a name="AllureTestOpsProject">Project in Allure TestOps</a>

<p align="center">
  <img src="resources/images/testops1.png" alt="Allure Report"/>
</p>

<p align="center">
  <img src="resources/images/testops2.png" alt="Allure Report"/>
</p>

<p align="center">
  <img src="resources/images/testops3.png" alt="Allure Report"/>
</p>


[Back to the table of contents ⬆](#TableOfContents)

# <a name="Jira">[Jira](https://jira.autotests.cloud/browse/HOMEWORK-423) integration</a>
> The link can be accessed only by authorized users.

<p align="center">
  <img src="resources/images/jira.png" alt="Jira integration"/>
</p>

[Back to the table of contents ⬆](#TableOfContents)


# <a name="Video">Video of running tests</a>

https://user-images.githubusercontent.com/95403808/201524887-0593a812-b18d-4a54-b8c9-440c7f2623ec.mp4

[Back to the table of contents ⬆](#TableOfContents)



