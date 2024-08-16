# Postmortem: Apache 500 Error - WordPress Website

## Issue Summary:

This postmortem details an Apache server issue causing a 500 Internal Server Error on a WordPress website. The outage occurred on Friday, August 16, 2024, from 10:00 AM to 10:30 AM PST. This affected 100% of users attempting to access the website, resulting in them seeing the generic 500 error message.

## Timeline:

10:00 AM PST: An engineer noticed a significant drop in website traffic through monitoring tools.
10:02 AM PST: The engineer confirmed the website was returning a 500 error upon manual testing.
10:05 AM PST: Initial investigation focused on Apache logs to identify any error messages.
10:10 AM PST: The investigation shifted towards potential issues with WordPress core files or plugins due to the lack of relevant Apache error messages.
10:15 AM PST: The decision was made to utilize strace in a separate tmux session to track Apache system calls during a website request.
10:20 AM PST: strace revealed an error during an attempt to access the wp-settings.php file.
10:25 AM PST: Manual inspection of wp-settings.php identified a typo where "phpp" was used instead of "php" within a configuration setting.
10:28 AM PST: A Puppet script was executed to fix the typo in wp-settings.php across all web servers.
Root Cause and Resolution:

The root cause of the 500 error was a typo in the wp-settings.php file. A configuration setting erroneously contained "phpp" instead of "php," likely due to a manual error during configuration or plugin installation. This typo caused an error during file access by Apache, resulting in the 500 error.

The resolution involved fixing the typo in wp-settings.php. A Puppet script was created to automate the fix across all web servers, ensuring consistent configuration.

## Corrective and Preventative Measures:

Improve Code Review Process: Implement a stricter code review process for manual configuration changes to catch typos and potential errors.
Version Control Configuration Files: Utilize version control systems like Git to manage configuration files like wp-settings.php. This allows for easier rollback and tracking of changes.
Automated Testing: Consider implementing automated tests for website functionality to identify regressions introduced by configuration changes.
Monitor Apache Logs: Enhance monitoring of Apache logs to capture more detailed error messages and improve early detection of issues.

## Lessons Learned:

This incident highlights the importance of thorough code reviews and configuration management. Utilizing strace for system call tracing proved effective in pinpointing the root cause of the Apache error. Implementing automated tests and improved logging can further strengthen the development and monitoring processes.
