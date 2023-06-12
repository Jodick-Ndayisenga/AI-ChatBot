# AI ChatBot

An AI chatbot is a computer program that uses artificial intelligence technology to simulate human conversation or interaction. These chatbots can understand natural language, interpret user intent, and use machine learning algorithms to improve their responses and interactions with users over time. They are commonly used in customer service, e-commerce, and other industries to provide 24/7 support and assistance to customers.

## OpenAI API
OpenAI API is a state-of-the-art artificial intelligence platform that provides easy-to-use interfaces for developers to build intelligent applications using the cutting-edge AI models developed by OpenAI.

In this ChatBot program, we have used OpenAI API for some specific purpose including text complition.

## Functionalities

When accessed, there appear a login page whereby if you have an account associated you can login, else you can create one after which you will be brought back to the login page.

Once logged in, the program filters only associated chats with user and loads the first three recent messages. There also appear input box where you can type a new question message or anything you want to ask our chat box.

## Fetch

Once a send button is clicked, JavaScript sends POST request to a python function with functionality of fetching from OPENAI. JavaScript sends both the question as a parameterand the waits for the response. Once fetch is over, chatbot returns a json object including the question, response and title of the question to JavaScript which in turns displays all of them to the user.

## What the chatbot can help:

1. provides a wide range of AI models, including natural language.

2. These models have been trained on large datasets and can be used to analyze, process, and generate natural language, images, and text. 

3. It can be used for a range of tasks, including language translation, text summarization, sentiment analysis, language modeling, and predictive text generation. 
4. It can also be used to generate realistic images, video, and audio content, as well as perform natural language conversation and question answering. 

5. Developers can access OpenAI API through a simple RESTful API, which can be integrated into any web or mobile application. 

6. It is designed to be highly scalable, and it can handle large volumes of requests and processes them in real-time.