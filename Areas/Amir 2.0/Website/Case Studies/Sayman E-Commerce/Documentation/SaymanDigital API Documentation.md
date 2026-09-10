---
created: 2026-09-10
doc_date: 2020-03-16
type: reference
source: SaymanDigital API Documentation.docx
topic: internal API spec
lang: fa
---

# SaymanDigital API Documentation

> [!info] About this note
> Internal REST API specification for the rebuilt (Laravel) SaymanDigital storefront — response conventions, endpoint list, and object schemas. Extracted from `SaymanDigital API Documentation.docx` (last touched 2020-03-16). Field/endpoint names and JSON are kept exactly as written; only the layout is reformatted (Word's flattened tables → Markdown tables/code blocks). Related: [[Sayman E-Commerce Case Study]] · [[Sayman — Website Case Study]]

## Business Api

### API Response Format

- Success (2xx)
- Not Succeeded (4xx, 5xx)

**نمونه برای آرایه‌ای از المنت‌ها**

```json
{
  "products": [
    {
      "id": 1,
      "name": "محصول 1"
    },
    {
      "id": 2,
      "name": "محصول 2"
    }
  ]
}
```

**نمونه یک المنت**

```json
{
  "product": {
      "id": 1,
      "name": "محصول 1"
    }
}
```

داده‌های با کلید پررنگ الزامی هستند.

**فرمت کلی ارور**

```json
{
  "code": 404,
  "message" : "محصول مورد نظر یافت نشد",
  "errors" : {}
}
```

**ارور Validation**

```json
{
  "code": 422,
  "message": "لطفا فیلد ها را بررسی کنید",
  "errors": {
    "title": [
      "فیلد عنوان اجباری است."
    ],
    "first_name": [
      "نام تنها میتواند شامل حروف و فاصله باشد"
    ]
  },
  "errors_list": [
    "فیلد عنوان اجباری است.",
    "نام تنها میتواند شامل حروف و فاصله باشد"
  ]
}
```

داده‌های با کلید پررنگ الزامی هستند.

> هشدار برای Front-End: هنگام خطای 500 ممکن است code و message از سمت سرور ارائه نشود.

## Resource Documentation

### User

| Method | Request | Params | Response |
|---|---|---|---|
| GET | `/profile/view` | — | `{ profile: {profile_object} }` |
| PATCH | `/profile/update` | `{ avatar: integer (multimedia id) }` | `{ message: __(profile.messages.update_success), profile: {profile_object} }` |
| GET | `/profile/invoices` | — | `{ invoices: [ {invoice_object}, ... ] }` |
| GET | `/profile/comments/` | `{ "type": "comment"/"question"/"answer" (default: comment), "status": "pending"/"published"/"spam" }` | `{ comments: [ {comment_object}, ... ] }` |
| GET | `/profile/bookmarks/` | `{ "type": "bookmark" }` | `{ products: [ {product_object_short}, {product_object_short}, ... ] }` |
| POST | `/user/login/` | `{ "phone": string, "password": string, "remember": string ("yes" or empty) }` | `{ token: {token_object}, profile: {profile_object} }` |
| POST | `/user/register/` | `{ "phone": string }` | `{ "message": __(user.registration.do_verify), "phone": string, "expire_time": timeStamp, "remaining_seconds": 60 }` |
| POST | `/user/register/confirm/` | `{ "phone": string, "verification_code": string }` | `{ "message": __(user.registration.verify_success), "phone": string, "token": {token_object}, "profile": {profile_object} }` |
| POST | `/user/register/data` | `{ "first_name": string, "last_name": string, "birthday": string (format: "1369/2/18"), "password": string, "avatar": integer (multimedia id), "email": email }` | `{ message: __(user.registration.data_success), profile: {profile_object} }` |
| POST | `/user/forget/` | `{ "phone": string }` | `{ "message": __(user.registration.do_verify), "phone": string, "expire_time": timeStamp, "remaining_seconds": 60 }` |
| POST | `/user/forget/confirm/` | `{ "phone": string, "verification_code": string }` | `{ "message": __(user.registration.restore_enter_new), "phone": string }` |
| POST | `/user/forget/newpassword/` | `{ "phone": string, "verify_code": string, "new_password": string, "new_password_confirm": string }` | `{ "message": __(user.registration.restore_success), "phone": string, "token": {token_object} }` |
| POST | `/user/logout/` | — | `{ message: __(user.logged_out) }` |

### Stores

| Method | Request | Params | Response |
|---|---|---|---|
| GET | `/stores` | `{ "count": 10 //(default), "start": 1 //(default) }` | `{ stores: [ {store_object}, {store_object}, ... ] }` |
| GET | `/stores/<id or slug>` | `{}` | `{ store: {store_object} }` |

### Products

| Method | Request | Params | Response |
|---|---|---|---|
| GET | `/products/<id or slug>` | `{ "include_similar": boolean (default: false), "include_related": boolean (default: false), "digest": false // short product (default: false) }` | `{ product: {product_object} }` |
| GET | `/products/<id>/similar` | `{ "count": integer (max & default: 10) }` | `{ products: [ {product_object_short}, ... ] }` |
| GET | `/products/<id>/related` | `{ "count": integer (max & default: 10) }` | `{ products: [ {product_object_short}, ... ] }` |
| GET | `/products/` | see below | see below |

**`GET /products/` params:**

```json
{
  "count": integer, // (default options.products_default_count)
  "start": integer, // (default 1)
  "product": string, // search both names
  "name": string,
  "name_en": string,
  "order": string (date, rating, expensiveness, cheapness),
  "in_stock": string ("yes" / "no"),
  "store": integer (id),
  "price_min": integer,
  "price_max": integer,
  "category": integer,
  "attributes": { "color": "red" },
  "url": sting,
  "on_sale": string ("yes" / "no"),
  "market_status": "available" / "discontinued" / "coming_soon"
}
```

**`GET /products/` response:**

```json
{
  "products": [
    {product_object_short},
    ...
  ],
  "filters": {
    "search": string,
    "in_stock": string,
    ...
  }
}
```

`filters` نشان‌دهنده فیلترهای اعمال‌شده در ریکوئست فعلی می‌باشد.

### Pages

| Method | Request | Params | Response |
|---|---|---|---|
| GET | `/pages/<slug>` | — | `{ page: {page_object} }` |
| POST | `/pages/contact/` | `{ name, subject, message, phone: mobile }` | success: `{ message: messages.contact.submitted }` · failure: `messages.contact.failed` |

### Sitemap

| Method | Request | Response |
|---|---|---|
| GET | `/sitemap/index` | `{ sitemapUrl: string, lastModified: timestamp }` |
| GET | `/sitemap/product/<pageID>` | `{ url: string, Images: integer, lastModified: timestamp }` |
| GET | `/sitemap/pages/<pageID>` | `{ url: string, Images: integer, lastModified: timestamp }` |
| GET | `/sitemap/stores/<pageID>` | `{ url: string, Images: integer, lastModified: timestamp }` |

### SiteOptions

| Method | Request | Params | Response |
|---|---|---|---|
| GET | `/options/<key>` | app name detected via header `app_name`; if not defined uses `"public"` for public options. Params: `{ app_name: string }` | `[ { Name: value } ]` |

### Category

| Method | Request | Params | Response |
|---|---|---|---|
| GET | `/categories/<id or slug>` | — | `{ "category": {category_object} }` |

## Object Reference

**Token**

```json
{
  access_token: string,
  refresh_token: string,
  expire_time: timestamp
}
```

**Profile**

```json
{
    "id": 1242,
    "name": "first user",
    "email": "koepp.sadie@example.org",
    "first_name": null,
    "last_name": null,
    "image": null,
    "phone": "091212345678",
    "last_login_at": null,
    "last_login_ip": null,
    "display_name": "first user",
    "avatar": "https://www.gravatar.com/avatar/513e60cababff8302b9a784991ec3f08"
}
```

**Comment**

```json
{
  id: integer,
  date: timeStamp,
  type: string,
  name: string,
  content: string,
  email: string,
  status: string,
  parent_id: integer,
  parent_user_name: string
}
```

**Product**

```json
{
  id: integer,
  name: string,
  price: decimal,
  price_offer: decimal | null,
  rating: decimal, // (1 to 5)
  stock_status: string, // in_stock, out_of_stock, backorder
  slug: string,
  market_status: string ("available"/"discontinued"/"coming_soon"),
  description: string,
  thumbnail: string (URL),
  last_updated: timeStamp,
  seo: {seo_object}
}
```

**Product_short**

```json
{
  id: integer,
  name: string,
  price: decimal,
  price_offer: decimal | null,
  rating: decimal, // (1 to 5)
  stock_status: string, // in_stock, out_of_stock, backorder
  slug: string,
  thumbnail: string (URL),
  last_updated: timeStamp
}
```

**Seo**

```json
{
  "title": string,
  "description": string,
  "keywords": array
}
```

**Invoice**

```json
{
  id: integer,
  date: timeStamp,
  description: string,
  status: string,
  transactions: [ {tranaction_object}, ... ]
}
```

**Transaction (incomplete)**

```json
{
  id: integer,
  ...
}
```

**Store**

```json
{
  "name": string,
  "domain": sting,
  "slug": string,
  "description": string,
  "comments": [ {comment_object}, ... ], // Last 20 comments
  "rating": 4.5,
  "image": string,
  "status": string
}
```

**Page**

```json
{
  "title": title,
  "content": content,
  ...
}
```

**Category**

```json
{
  name: string,
  slug: string,
  description: string,
  parentId: integer
}
```

---

## یادداشت‌های من

- سند خودش اذعان می‌کند `Transaction` ناقص است («incomplete»).
- چند تایپوی جزئی در سند اصلی دست‌نخورده باقی مانده: `tranaction_object` (باید transaction_object باشد) و `sting` به‌جای string (در دو جا: `url` و `domain`).
