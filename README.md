# Adapt-Fitbit
Repository for ADAPT fitbit data collection tools used for autonomous collection prodcedures

## 1. Pull the Fitbit API connection code, and open it in your IDE of choice
> When you pull the code, you will have two examples of what the data should look like whenever you execute the file, both in HTML format. You should move these to a different file, and then execute the code again (after the connection is made in the next steps) in order to compare the files and make sure they are the same format.
>
> [Example of heart rate HTML](https://github.com/JaxonBauer/Adapt-Fitbit/blob/main/heart_rate_data.html)
>
> [Example of sleep data HTML](https://github.com/JaxonBauer/Adapt-Fitbit/blob/main/sleep_data.html)

## 2. Create a fitbit account (if you do not have one already)
> This will allow you to create a fitbit account (and allow you to register a device as well) if you haven't already, giving you a test connection to implement into the application th make sure the connections work properly.

## 3. Create a dev account through Fitbit, and create a new web application using the applications page
> Please refer to the [Getting Started with Fitbit API](https://dev.fitbit.com/build/reference/web-api/) document to see how to set up your application for server access
>
>[Fitbit Development Applications Page](https://dev.fitbit.com/apps)

## 4. Read the documentation on OAuth 2.0 for Fitbit device networks here
> [Fitbit OAuth 2.0 Tutorial](https://dev.fitbit.com/build/reference/web-api/troubleshooting-guide/oauth2-tutorial/)

## Important Things To Note
> The current implementation is set up for a personal server, which means that it does not support multiple Fitbit device endpoint connections. In order to do this, a new app must be created following the procedures given as examples in the following link.
>
> [OAuth 2.0 Libraries and Sample Code](https://dev.fitbit.com/build/reference/web-api/developer-guide/libraries-and-sample-code/)
>
> The functionality of the code is set up to be compatible with a new server-side application, as well as the current personal implementation.
>
> In order to get the connection to work for API implementation, you need to create a .env file that contains the following variables, initializing them to whatever values are gathered from the OAuth 2.0 process.
>
> Below is a representation of what the .env file should look like:
![image](https://github.com/JaxonBauer/Adapt-Fitbit/assets/103966964/58c705e7-015e-4d49-91ed-2ac07a9b0ebb)
