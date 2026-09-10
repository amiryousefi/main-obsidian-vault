---
created: 2026-09-10
type: sprint-report
sprint_number: 8
source: گزارش اسپرینت شماره 8.xlsx
date_range_shamsi: ۱۶ تا ۲۸ آذر ۱۳۹۸
date_range_gregorian: 2019-12-07 to 2019-12-19
---

# اسپرینت ۸ — گزارش

> [!info] درباره این نوت
> گزارش خام اسپرینت شماره ۸ (۱۶ تا ۲۸ آذر ۱۳۹۸ / ۷ تا ۱۹ دسامبر ۲۰۱۹) از بازسازی فروشگاه اینترنتی سایمان دیجیتال با لاراول، استخراج‌شده از `گزارش اسپرینت شماره 8.xlsx`. مرتبط: [[Sayman — Website Case Study]] · [[Sayman E-Commerce Case Study]]

## خلاصه

**بازه:** ۱۶ تا ۲۸ آذر ۱۳۹۸ (۷ تا ۱۹ دسامبر ۲۰۱۹).

توجه: ستون «ساعت کاری گزارش‌شده» در برگه اصلی اکسل عددی بسیار کوچک‌تر از حد انتظار نشان می‌دهد (مثلاً چند ساعت در کل اسپرینت، در حالی که ساعات برنامه‌ریزی‌شده در همان ردیف دهها تا صدها ساعت است). این به‌نظر یک خطای فرمول در فایل اکسل اصلی است (احتمالاً میانگین یا تقسیم نادرست)، نه ساعت واقعی کار انجام‌شده؛ عدد همان‌طور که در فایل اصلی بود، بدون اصلاح، در جدول زیر آمده است. برای سنجش واقعی پیشرفت، از ستون‌های «تعداد تسک انجام‌شده» و «درصد تسک انجام‌شده» استفاده کنید.

نرخ تکمیل تسک مجموع این اسپرینت ٪۸۴ است. توجه: ردیف امیر یوسفی «تعداد روز حضور: ۰» دارد اما «ساعات کاری برنامه‌ریزی شده: ۸.۵» و «تعداد تسک انجام‌شده: ۴» — به نظر می‌رسد حضور فیزیکی کم بوده اما کار از راه دور ثبت شده است.

| مورد | مقدار |
|---|---|
| ظرفیت کاری اسپرینت | 352.5 ساعت |
| میانگین ساعات کاری | - |
| تعداد روز حضور | 47 |
| میزان ساعات کاری حضور | 352.5 |
| ساعات کاری برنامه‌ریزی شده | 355 |
| تعداد تسک برنامه‌ریزی‌شده | 108 |
| ساعت کاری گزارش‌شده | 14.38888889 |
| اختلاف گزارش شده با برنامه‌ریزی‌شده | - |
| تعداد تسک انجام‌شده | 91 |
| درصد تسک انجام‌شده | 0.8425925926 |

## اطلاعات آماری

- **ظرفیت کاری اسپرینت:** 352.5 ساعت
- **تاریخ شروع (شمسی):** 16 آذر 1398
- **تاریخ پایان (شمسی):** 28 آذر 1398

| شخص | میانگین ساعات کاری | تعداد روز حضور | میزان ساعات کاری حضور | ساعات کاری برنامه‌ریزی شده | تعداد تسک برنامه‌ریزی‌شده | ساعت کاری گزارش‌شده | اختلاف گزارش شده با برنامه‌ریزی‌شده | تعداد تسک انجام‌شده | درصد تسک انجام‌شده |
|---|---|---|---|---|---|---|---|---|---|
| سالار قلی‌زاده | 7.5 | 12.0 | 90 | 88.5 | 28 | 3.727777777777778 | 0.0 | 24 | 0.8571428571 |
| فرهاد حسن‌پور | 7.5 | 11.0 | 82.5 | 79.5 | 20 | 3.502083333333333 | 0.0 | 20 | 1 |
| سینا یک روی | 7.5 | 12.0 | 90 | 84.5 | 34 | 3.423611111111111 | 0.0 | 27 | 0.7941176471 |
| هانیه تربیت | 7.5 | 12.0 | 90 | 94 | 22 | 3.7354166666666666 | 0.0 | 16 | 0.7272727273 |
| امیر یوسفی | 7.5 | 0.0 | 0 | 8.5 | 4 | 0.0 | 0.0 | 4 | 1 |
| مجموع | - | 47 | 352.5 | 355 | 108 | 14.38888889 | - | 91 | 0.8425925926 |

## برنامه کاری

| شرح کار | سالار قلی‌زاده | فرهاد حسن‌پور | هانیه تربیت | سینا یک روی | امیر یوسفی |
|---|---|---|---|---|---|
| حذف روت product/bulk/tags/search |  | 2.0 |  |  |  |
| حذف روت product/bulk/update |  | 2.0 |  |  |  |
| delete route user/search |  | 3.0 |  |  |  |
| delete group/search |  | 2.0 |  |  |  |
| update route invoices/send/sms |  | 0.5 |  |  |  |
| consider default in slug checker switch case |  | 0.5 |  |  |  |
| enhance product bulk routes like admin in vendors |  | 1.0 |  |  |  |
| delete product/bulk/tags/searh in vendor |  | 1.0 |  |  |  |
| delete route product/get-categories in  vendor |  | 1.0 |  |  |  |
| confirm before acounting confirmation |  | 1.0 |  |  |  |
| dictionary for products english to farsi name converting |  | 2.0 |  |  |  |
| vendor login |  |  |  | 4.0 |  |
| vendor permissions |  |  |  | 6.0 |  |
| update ordergroup to invoice group |  | 2.0 |  |  |  |
| show created_at in invoice groups |  | 0.5 |  |  |  |
| add logo, status, priority to payment methods, credentials |  | 10.0 |  |  |  |
| make filters shown in url parameters | 5.0 |  |  |  |  |
| store and show archive date |  | 1.5 |  |  |  |
| date filters for payment date, completed and .... | 5.0 |  |  |  |  |
| store any status change date(paid_at, completed_at , ...( | 5.0 |  |  |  |  |
| search user by email, phone, name and last name | 1.0 |  |  |  |  |
| search invoice by id code, phone, bank card | 2.0 |  |  |  |  |
| filter invoices that have shipment tracking code | 1.0 |  |  |  |  |
| filter invoices by shipment method | 1.0 |  |  |  |  |
| show customer, description, status in index | 1.0 |  |  |  |  |
| filter invoicses by transactions | 0.5 |  |  |  |  |
| filter invoices with no invoice group | 1.0 |  |  |  |  |
| show store in invoice index | 2.0 |  |  |  |  |
| add sku for variation | 2.0 |  |  |  |  |
| discount price with dates in variations | 4.0 |  |  |  |  |
| editable price for invoice line price | 8.0 |  |  |  |  |
| Solve total price calucaltion bug | 2.0 |  |  |  |  |
| show invoice line discount and total discount in invoice | 5.0 |  |  |  |  |
| colors for KYC scores | 2.0 |  |  |  |  |
| shipment price calculation | 2.0 |  |  |  |  |
| refund invoice( full refund, partial refund for invoice line) | 20.0 |  |  |  |  |
| variations tests | 3.0 |  |  |  |  |
| varitaion -> short name attribute | 0.5 |  |  |  |  |
| product -> short name attribute | 0.5 |  |  |  |  |
| make audit morhable |  |  |  | 2.0 |  |
| create observers for audit |  |  |  | 4.0 |  |
| create trait for audit observers |  |  |  | 2.0 |  |
| make audit main function to get: message, action, data |  |  |  | 3.0 |  |
| audit documentation |  |  |  | 1.0 |  |
| complete filters in variations( like products list) |  |  |  | 10.0 |  |
| separete columns for attrs like color and gurantee in variations |  |  |  | 8.0 |  |
| change short description to textarea |  |  |  | 0.5 |  |
| confirm befor delete |  |  |  | 0.5 |  |
| filter bundle product |  |  |  | 0.5 |  |
| filter stores |  |  |  | 1.5 |  |
| autocomplete off in filter fields specially for date fields |  |  |  | 0.5 |  |
| auto slug generation |  |  |  | 2.0 |  |
| link to products list by a tag in tags index with product count |  |  |  | 2.0 |  |
| filter by tags |  |  |  | 2.0 |  |
| show image after upload in brand |  |  |  | 2.0 |  |
| helper for making arabic and farsi conflicintg characters standard + middleware |  |  |  | 3.0 |  |
| add section for attributes |  |  |  | 2.0 |  |
| add loading for getting attributes from crawler |  |  |  | 0.5 |  |
| select2 ajax for category and tag filters |  |  |  | 2.0 |  |
| show store coutns in index |  |  |  | 1.0 |  |
| ajax select2 for parent category |  |  |  | 0.5 |  |
| created_at in index |  |  |  | 0.5 |  |
| link to products list by a category in categories index with product count |  |  |  | 1.0 |  |
| ajax select2 for user select in stores  create |  |  |  | 1.0 |  |
| excel export in invoice index |  |  |  | 3.0 |  |
| public notes in invoices to send for users |  |  |  | 2.0 |  |
| dynamic views in indexes by user definition(datatables) |  |  |  | 7.0 |  |
| حالت موبایل مشخصات محصول |  |  | 3.0 |  |  |
| حالت موبایل چارت |  |  | 4.0 |  |  |
| حالت موبایل کامنت |  |  | 3.0 |  |  |
| حالت موبایل پرسش و پاسخ |  |  | 3.0 |  |  |
| حالت موبایل فروشندگتن محصول |  |  | 5.0 |  |  |
| حالت موبایل vote |  |  | 2.0 |  |  |
| مدال چارت |  |  | 4.0 |  |  |
| مدال گالری |  |  | 6.0 |  |  |
| مدال هشدار |  |  | 4.0 |  |  |
| حالت موبایل مدال چارت |  |  | 7.0 |  |  |
| حالت جستجوی هدر |  |  | 4.0 |  |  |
| صفحه مقایسه: قسمت نمایش محصولات |  |  | 2.0 |  |  |
| صفحه مقایسه: قسمت جزئیات محصولات |  |  | 4.0 |  |  |
| صفحه لیست محصولات |  |  | 10.0 |  |  |
| تگ های صفحه |  |  | 4.0 |  |  |
| حالت گرید به لیست |  |  | 3.0 |  |  |
| ساخت کامپوننت نمایش لیستی |  |  | 6.0 |  |  |
| حالت موبایل نتایج لیست جستجوها |  |  | 6.0 |  |  |
| منو حالت موبایل |  |  | 7.5 |  |  |
| پیاده‌سازی رابط کاربری فعلی به صورت فایل‌های بلید |  | 41.0 |  |  |  |
| کمک به پیاده‌سازی رابط کاربری فعلی | 1.5 |  |  |  |  |
| جلسه برنامه ریزی موارد کاری باقی مانده | 2.0 | 2.0 |  | 2.0 | 2.0 |
| جلسه برنامه ریزی اسپرینت | 4.0 | 4.0 | 4.0 | 4.0 | 4.0 |
| فیکس باگ نمایش عکس در کامپوننت آپلود عکس |  |  |  | 2.0 |  |
| آماده سازی صفحات مربوط به یلدای سایمان دیجیتال | 5.0 |  |  |  |  |
| جلسه توضیحات مربوط به تامین کنندگان در سیستم جدید با پژمان | 1.0 | 1.0 | 1.0 |  | 1.0 |
| جلسه همفکری در مورد sayman digital hub | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 |

## گزارش کاری

| شرح کار | سالار قلی‌زاده | فرهاد حسن‌پور | هانیه تربیت | سینا یک روی | امیر یوسفی |
|---|---|---|---|---|---|
| حذف روت product/bulk/tags/search |  | 1 |  |  |  |
| حذف روت product/bulk/update |  | 1 |  |  |  |
| delete route user/search |  | 1 |  |  |  |
| delete group/search |  | 1 |  |  |  |
| update route invoices/send/sms |  | 1 |  |  |  |
| consider default in slug checker switch case |  | 1 |  |  |  |
| enhance product bulk routes like admin in vendors |  | 1 |  |  |  |
| delete product/bulk/tags/searh in vendor |  | 1 |  |  |  |
| delete route product/get-categories in  vendor |  | 1 |  |  |  |
| confirm before acounting confirmation |  | 1 |  |  |  |
| dictionary for products english to farsi name converting |  | 1 |  |  |  |
| vendor login |  |  |  | 1 |  |
| vendor permissions |  |  |  | 1 |  |
| update ordergroup to invoice group |  | 1 |  |  |  |
| show created_at in invoice groups |  | 1 |  |  |  |
| add logo, status, priority to payment methods, credentials |  | 1 |  |  |  |
| make filters shown in url parameters | 1 |  |  |  |  |
| store and show archive date |  | 1 |  |  |  |
| date filters for payment date, completed and .... | 1 |  |  |  |  |
| store any status change date(paid_at, completed_at , ...( | 1 |  |  |  |  |
| search user by email, phone, name and last name | 1 |  |  |  |  |
| search invoice by id code, phone, bank card | 1 |  |  |  |  |
| filter invoices that have shipment tracking code | 1 |  |  |  |  |
| filter invoices by shipment method | 1 |  |  |  |  |
| show customer, description, status in index | 1 |  |  |  |  |
| filter invoicses by transactions | 1 |  |  |  |  |
| filter invoices with no invoice group | 1 |  |  |  |  |
| show store in invoice index | 1 |  |  |  |  |
| add sku for variation | 1 |  |  |  |  |
| discount price with dates in variations | 0 |  |  |  |  |
| editable price for invoice line price | 1 |  |  |  |  |
| Solve total price calucaltion bug | 0 |  |  |  |  |
| show invoice line discount and total discount in invoice | 0 |  |  |  |  |
| colors for KYC scores | 1 |  |  |  |  |
| shipment price calculation | 1 |  |  |  |  |
| refund invoice( full refund, partial refund for invoice line) | 0 |  |  |  |  |
| variations tests | 1 |  |  |  |  |
| varitaion -> short name attribute | 1 |  |  |  |  |
| product -> short name attribute | 1 |  |  |  |  |
| make audit morhable |  |  |  | 1 |  |
| create observers for audit |  |  |  | 1 |  |
| create trait for audit observers |  |  |  | 1 |  |
| make audit main function to get: message, action, data |  |  |  | 1 |  |
| audit documentation |  |  |  | 1 |  |
| complete filters in variations( like products list) |  |  |  | 1 |  |
| separete columns for attrs like color and gurantee in variations |  |  |  | 0 |  |
| change short description to textarea |  |  |  | 1 |  |
| confirm befor delete |  |  |  | 1 |  |
| filter bundle product |  |  |  | 1 |  |
| filter stores |  |  |  | 1 |  |
| autocomplete off in filter fields specially for date fields |  |  |  | 1 |  |
| auto slug generation |  |  |  | 1 |  |
| link to products list by a tag in tags index with product count |  |  |  | 1 |  |
| filter by tags |  |  |  | 1 |  |
| show image after upload in brand |  |  |  | 1 |  |
| helper for making arabic and farsi conflicintg characters standard + middleware |  |  |  | 0 |  |
| add section for attributes |  |  |  | 0 |  |
| add loading for getting attributes from crawler |  |  |  | 1 |  |
| select2 ajax for category and tag filters |  |  |  | 1 |  |
| show store coutns in index |  |  |  | 0 |  |
| ajax select2 for parent category |  |  |  | 1 |  |
| created_at in index |  |  |  | 1 |  |
| link to products list by a category in categories index with product count |  |  |  | 1 |  |
| ajax select2 for user select in stores  create |  |  |  | 1 |  |
| excel export in invoice index |  |  |  | 0 |  |
| public notes in invoices to send for users |  |  |  | 0 |  |
| dynamic views in indexes by user definition(datatables) |  |  |  | 0 |  |
| حالت موبایل مشخصات محصول |  |  | 1 |  |  |
| حالت موبایل چارت |  |  | 1 |  |  |
| حالت موبایل کامنت |  |  | 1 |  |  |
| حالت موبایل پرسش و پاسخ |  |  | 1 |  |  |
| حالت موبایل فروشندگان محصول |  |  | 1 |  |  |
| حالت موبایل vote |  |  | 1 |  |  |
| مدال چارت |  |  | 1 |  |  |
| مدال گالری |  |  | 1 |  |  |
| مدال هشدار |  |  | 1 |  |  |
| حالت موبایل مدال چارت |  |  | 1 |  |  |
| حالت جستجوی هدر |  |  | 1 |  |  |
| صفحه مقایسه: قسمت نمایش محصولات |  |  | 1 |  |  |
| صفحه مقایسه: قسمت جزئیات محصولات |  |  | 0 |  |  |
| صفحه لیست محصولات |  |  | 0 |  |  |
| تگ های صفحه |  |  | 1 |  |  |
| حالت گرید به لیست |  |  | 0 |  |  |
| ساخت کامپوننت نمایش لیستی |  |  | 0 |  |  |
| حالت موبایل نتایج لیست جستجوها |  |  | 0 |  |  |
| منو حالت موبایل |  |  | 0 |  |  |
| پیاده‌سازی رابط کاربری فعلی به صورت فایل‌های بلید |  | 1 |  |  |  |
| کمک به پیاده‌سازی رابط کاربری فعلی | 1 |  |  |  |  |
| جلسه برنامه ریزی موارد کاری باقی مانده | 1 | 1 |  | 1 | 1 |
| جلسه برنامه ریزی اسپرینت | 1 | 1 | 1 | 1 | 1 |
| فیکس باگ نمایش عکس در کامپوننت آپلود عکس |  |  |  | 1 |  |
| آماده سازی صفحات مربوط به یلدای سایمان دیجیتال | 1 |  |  |  |  |
| جلسه توضیحات مربوط به تامین کنندگان در سیستم جدید با پژمان | 1 | 1 | 1 |  | 1 |
| جلسه همفکری در مورد sayman digital hub | 1 | 1 | 1 | 1 | 1 |

## جلسه بازنگری (Retrospective)

| آموخته‌های اسپرینت، موانع و مشکلات گزارش‌شده، راهکارهای بهبود عملکرد |
|---|
| امیر: در صورت بروز باگ یا گیر کردن روی تسکی بیشتر از یک ساعت سویچ کنید روی تسک یا فضای کاری دیگه. |
| سالار: ایونت ها رو برای دقیقه نود نگه نداریم و از هفته پیش یا قبل از شروع اسپرینت برنامه ریزی کنیم. |
| هانیه: API برای پروژه عیار به سرعت انجام تسک‌ها و هم جلوگیری از دوباره کاری کمک می‌کند. |
| امیر: مسئول برررسی مرج ریکوئست‌ها همه اعضای تیم می توانند باشند. سالار و امیر امکان مرج دارند. بعد از مرج ریکوئست امیر یا سالار موظف هستند تا ۵ دقیقه خود یا نفر مقابل را به مرج ریکوئست اساین کنند. |
| سینا: بهتر است امیر تا جای ممکن جزئیات تسک ها را قبل از جلسه برنامه ریزی اسپرینت در بیاورد. |
| فرهاد: اولویت بندی تسک ها به ترتیب اهمیت مشخص شود. همچنین اولویت انجام تسک‌ها مشخص شود. |
| گروه: بریک‌‌های کوتاه بین کارها به افزایش تمرکز کمک می‌کند |
