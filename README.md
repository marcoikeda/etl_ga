# etl_ga
A lot of companies are relying on Google Analytics Free for tracking and marketing investment optimization. This code aims to give a quick workaround on how to extract path-to-purchase data, either to integrate it in DMPs or to run attribution models.

##### Overview
1 - Implement cookie and timestamp tracking with custom dimension

2 - Get GA API key

3 - Extract data using google2pandas

4 - Transform data

##### 1 - Implement cookie and timestamp tracking with custom dimension:
First you need to create two custom dimensions in your Google Analytics account.

Dimension1 = browser_id (user)

Dimension2 = timestamp (hit)

In the website code, add the following lines:
```
ga('require', 'ecommerce');
ga(function(tracker) {
      var clientId = tracker.get('clientId');
      ga('set', 'dimension1', clientId);
      ga('set', 'dimension2', new Date().getTime());
      ga('send', 'pageview');
      ga('ecommerce:addTransaction', {
          'id': Math.floor((Math.random() * 1000) + 1),                     // Transaction ID. Required.
          'affiliation': 'Acme Clothing',   // Affiliation or store name.
          'revenue': '11.99',               // Grand Total.
          'shipping': '5',                  // Shipping.
          'tax': '1.29'                     // Tax.
        });
ga('ecommerce:send');
```

##### 2 - Get GA API key

https://developers.google.com/analytics/devguides/config/mgmt/v2/authorization

##### 3 - Extract data using google2pandas
Make sure you have properly installed google2pandas module.




##### Appendix: List of marketing channels used:
###### Search (Google):
?utm_source=google&utm_medium=cpc&utm_campaign=test

utm_source = google

utm_medium = cpc

utm_campaign = test

###### Social (Facebook):
?utm_source=fb&utm_medium=social&utm_campaign=test

utm_source = fb

utm_medium = social

utm_campaign = test

###### Display (UOL):
?utm_source=uol&utm_medium=display&utm_campaign=test

utm_source = uol

utm_medium = display

utm_campaign = test

###### Affiliates (blog):
?utm_source=blog&utm_medium=affiliate&utm_campaign=test

utm_source = blog

utm_medium = affiliate

utm_campaign = test
