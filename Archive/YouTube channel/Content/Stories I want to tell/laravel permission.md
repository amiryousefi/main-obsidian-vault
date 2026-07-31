---
status: in-progress
base: "[[Stories I want to tell.base]]"
---

### Permission issue

In any web project you need to take care of permissions and what routes and feature a user could access. There is a lot of ways to do this but for a long time I was using this method of mine that is easy and flexible to implement and almost had no effects in your ongoing development and codes. Like you solve the permissions and authorization concerns with this approach and you just forget about it while you continue on developing.

### Medium Article

I used this approach in many production level projects. So I decided to write about this method and share my experience. I had a Medium article where I explained about this approach and this article gained a lot of interests.

### GitHub repo

So I developed a Laravel package to enhance the codes I used and also to be able to develop this as an independent project. Now you can see whole source code in my GitHub or use this package via composer. This way it's more easier to use and also extend or override some of the classes and codes I developed to your own usage.

### Code explanation intro

This is a sample project I made to just show you how to use this package in your projects.
I have two simple routes, one to get a product list and one to get a product details. This is just simple basic functions and there is no real logic here. So let's have a deep look into this.

### Call to Action