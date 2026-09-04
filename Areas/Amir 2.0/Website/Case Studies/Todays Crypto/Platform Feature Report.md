---
created: 2026-08-25
---

# TodaysCrypto — Platform Feature Report

> **Date:** May 8, 2026  
> **Platform type:** Crypto-focused video sharing platform (YouTube-like)  
> **Architecture:** Three-part system — Web App · Backend API · Publisher & Admin Panel

---

## Table of Contents

1. [Platform Overview](#1-platform-overview)
2. [Technology Stack](#2-technology-stack)
3. [Web App (`ox-tv-front-next`)](#3-web-app-ox-tv-front-next)
4. [Backend API (`TC-backend`)](#4-backend-api-tc-backend)
5. [Publisher & Admin Panel (`tc-publisher-panel`)](#5-publisher--admin-panel-tc-publisher-panel)
6. [Cross-Cutting Features](#6-cross-cutting-features)
7. [API Endpoint Reference](#7-api-endpoint-reference)

---
## 1. Platform Overview

TodaysCrypto (TC) is a video-sharing platform purpose-built for the cryptocurrency and blockchain community. It combines traditional video platform features (upload, watch, subscribe, comment, playlists) with crypto-native capabilities including Web3 wallet authentication, a native platform token (TCG), NFT-based memberships, cryptocurrency market data, and crypto-focused ad campaigns.

### Three Sub-Systems

| Part | Directory | Framework | Role |
|------|-----------|-----------|------|
| Web App | `ox-tv-front-next` | Next.js 12 / React 17 | Public-facing viewer experience |
| Backend | `TC-backend` | Laravel 8 (PHP 8) | REST API, business logic, database |
| Publisher & Admin Panel | `tc-publisher-panel` | React 17 / CRA | Creator dashboard + admin back-office |

---

## 2. Technology Stack

### Web App
- **Framework:** Next.js 12 (server-side rendering + static generation)
- **UI:** React 17, Tailwind CSS 2, CSS Modules
- **State / Data:** React Query, custom hooks
- **Video:** Native HTML5 video player (custom implementation)
- **Web3:** wagmi, ethers.js, Web3Modal, MetaMask Jazzicon
- **Payments:** Stripe React SDK
- **Real-time:** Pusher JS
- **Charts:** Chart.js
- **Carousel:** Swiper, React Slick

### Backend
- **Framework:** Laravel 8 (PHP 7.3 / 8.0)
- **Primary DB:** MySQL (via Eloquent ORM)
- **Secondary DB:** MongoDB (watch times, token points, channel statistics)
- **Cache / Queue:** Redis (Predis)
- **Auth:** Laravel Passport (OAuth 2.0), JWT-like tokens
- **Real-time:** Laravel WebSockets + Pusher
- **Storage:** AWS S3, Cloudflare R2 (video files), local disk
- **Video Processing:** php-ffmpeg (duration extraction)
- **PDF Export:** barryvdh/laravel-dompdf
- **Payments:** Laravel Cashier (Stripe), Coinbase Commerce
- **Subtitles:** mantas-done/subtitles library
- **QR Codes:** bacon/bacon-qr-code (for Google 2FA)
- **KYC:** Idenfy identity verification
- **Image Processing:** Intervention Image
- **Excel Export:** Maatwebsite/Excel

### Publisher & Admin Panel
- **Framework:** React 17, Create React App (CRA + CRACO)
- **Routing:** React Router v5
- **UI:** Tailwind CSS, CSS Modules
- **Data:** React Query, Axios
- **Video Player:** Video.js with Overlay plugin
- **Charts:** Chart.js
- **Real-time:** Pusher JS
- **Web3:** ethers.js

---

## 3. Web App (`ox-tv-front-next`)

The public-facing web application is fully responsive with separate mobile and desktop component trees per page.

### 3.1 Pages & Routes

| Route | Description |
|-------|-------------|
| `/` | Home — trending videos, top channels, personalised "For You" feed |
| `/channels` | Channels listing |
| `/channels/[slug]` | Channel detail page |
| `/category/[slug]` | Category listing |
| `/search` | Search results |
| `/show/[url_hash]` | Video / Podcast watch page |
| `/playlists/[url_hash]` | Playlist view |
| `/podcasts` | Podcast listing |
| `/markets/[slug]` | Cryptocurrency market detail |
| `/tcg` | TCG (TodaysCrypto Token) overview page |
| `/lottery` | Platform lottery page |
| `/membership` | Hero Membership plans & subscription |
| `/membership/membership` | Membership detail / purchase flow |
| `/advertisers` | Advertiser inquiry & information |
| `/about` | About page |
| `/faq` | FAQ |
| `/governance` | Governance |
| `/privacy` | Privacy policy |
| `/tos` | Terms of service |
| `/login` | Login (email + magic link + Web3 wallet) |
| `/register` | Registration (email + Web3 wallet) |
| `/password` | Forgot / reset password |
| `/verify` | Email verification |
| `/m/wallet` | Web3 wallet connection (mobile) |
| `/m/login-with-wallet` | Wallet login (mobile) |
| `/m/register-with-wallet` | Wallet register (mobile) |
| `/me` | User profile dashboard |
| `/me/edit` | Edit profile |
| `/me/feed` | Personalised feed |
| `/me/subscriptions` | Subscribed channels |
| `/me/subscriptions/[slug]` | Subscription channel detail |
| `/me/bookmarks` | Bookmarked videos |
| `/me/playlists` | User playlists |
| `/me/notifications` | Notifications |
| `/me/security` | Security settings (2FA, password) |
| `/me/referral` | Referral programme |
| `/me/earn` | Earnings via share links |
| `/me/tcg` | TCG token balance & history |
| `/me/payments` | Payment & transaction history |
| `/me/oldMessages` | Legacy messages |
| `/me/delete` | Delete account |
| `/publisher` | Publisher landing / redirect |
| `/404`, `/403`, `/video404` | Error pages |

### 3.2 Home Page

- Trending videos (cached, updated hourly)
- Trending channels
- Top channels
- Latest media (mixed video + podcasts)
- Personalised "For You" feed (based on favourite cryptocurrency tags and user preferences)
- Separate mobile and desktop layouts

### 3.3 Video Watch Page

- Video player with custom UI (native HTML5 + Web3 enhancements)
- Like / Dislike
- Bookmark video
- Add to playlist
- Report video
- Share (generates shareable link with view tracking)
- View counter (rate-limited WAF-protected endpoint)
- Watch-time tracking (posted to backend for monetisation calculation)
- Related videos sidebar
- Chapters navigation
- Subtitles (multi-language)
- End-screen card overlays (VideoMeta "layers")
- Comments section with nested replies
- Comment like / dislike
- Comment pin (for channel owners)
- Comment reporting

### 3.4 Channel Pages

- Channel header (banner, avatar, subscriber count, description)
- Channel video listing
- Channel playlists
- Subscribe / Unsubscribe button
- Channel statistics (views, subscribers)

### 3.5 Search

- Keyword search across video titles, descriptions, tags
- Filters: media type (video / podcast), time period
- Channel results alongside video results
- Minimum 3-character keyword for tag search

### 3.6 Discover / Browse

- Category-based browsing
- Markets page (cryptocurrency market data, historical prices)
- Podcasts-only listing

### 3.7 User Profile & Account (`/me`)

- **Profile editing** — username, avatar, bio, ETH address, wallet address
- **Personalised feed** — custom feed based on selected preferences
- **Subscriptions** — manage subscribed channels, view subscribed-channel videos
- **Bookmarks** — saved/bookmarked videos
- **Playlists** — create, edit, delete user playlists; add/remove videos
- **Notifications** — list and mark notifications as read
- **Security** — change password, enable/disable Email 2FA, enable/disable Google Authenticator (TOTP) with QR code
- **Referral programme** — referral link, statistics, point activation
- **Earn** — earnings via video share links (share-link statistics)
- **TCG tokens** — token balance, locked vs unlocked tokens, daily watch limit status
- **Payments** — transaction and membership payment history
- **Account deletion** — soft-delete with 2FA/email verification gate, restore via token link

### 3.8 Authentication

- Email + password registration and login
- Magic link login (passwordless, email-based)
- Web3 / Ethereum wallet login (MetaMask + WalletConnect via Web3Modal)
- Web3 wallet registration
- Password reset via email link
- Email verification flow
- 2FA gate on sensitive operations

### 3.9 Membership (Hero Membership)

- Tiered paid membership plans
- Payment via Stripe (card) or Coinbase (crypto)
- NFT-based Hero status detection (TC Polygon smart contract listener)
- Membership data displayed on user profile

### 3.10 TCG Token Page

- Token overview: total supply, total distributed, today distributed
- User token balance (unlocked vs locked)
- Daily watch limit tracker
- Token distribution statistics (daily / monthly)

### 3.11 Lottery Page

- Active lottery listing (public)

### 3.12 Advertisers Page

- Advertiser information and inquiry form

### 3.13 Cryptocurrency Markets

- Market data listing with historical price charts
- Favourite cryptocurrency management (add/remove)
- Click-to-buy campaign integration (crypto campaigns)

---

## 4. Backend API (`TC-backend`)

The backend is a Laravel 8 REST API with role-based access control (user / publisher / admin). All routes are under `/api/*`.

### 4.1 Authentication & Security

| Feature | Details |
|---------|---------|
| Registration | Email + password with rate limiting (3 per 200h) |
| Login | Email/password, scoped (admin, publisher, user) |
| Magic Link Login | Email-based passwordless, scoped |
| Web3 Login | Ethereum wallet signature verification (Keccak-256) |
| Web3 Registration | Wallet-based account creation |
| Laravel Passport | OAuth 2.0 token management (with Redis token caching) |
| 2FA — Email | OTP sent to email; enable/disable via API |
| 2FA — Google | TOTP with QR code; enable/disable with hard 2FA check |
| Password Reset | Email token, verify token, reset endpoint |
| Email Verification | Token-based email confirm flow |
| KYC (Idenfy) | Identity verification URL, webhook handler |
| WAF | Rate limiting, suspicious IP blocking, bad request logging |
| Captcha | Image captcha generate + verify |

### 4.2 Video

| Feature | Details |
|---------|---------|
| Media types | `video` and `podcast` |
| Upload methods | Direct upload to S3 / Cloudflare R2 (pre-signed URLs), direct server upload |
| Video statuses | `draft`, `draft_yi` (YouTube import draft), `published`, `archived`, `suspended`, `hidden` |
| File types | Video file or audio file |
| Duration extraction | Automatic via ffmpeg on upload |
| URL hash | Auto-generated unique 12-character public identifier |
| View counter | Rate-limited, WAF-protected; separate watch-time store |
| Watch-time tracking | Stored in MongoDB; used for token and monetisation calculation |
| Like / Dislike | Authenticated users; toggle behaviour |
| Bookmark | Authenticated users; bookmarks listing |
| Report | Authenticated users; reports video |
| Share links | Generate unique share links; track views and click counts |
| Related videos | Served based on category / tags |
| Subscribed-channel videos | Feed of videos from subscribed channels |
| Publisher CRUD | Create, update, delete, bulk delete, publish, bulk-pin |
| Admin controls | Hide, unhide, bulk assign category |
| YouTube Importer | Manual import, auto-import toggle, sync request, import stats |

### 4.3 Video Metadata

| Feature | Details |
|---------|---------|
| Chapters | Create, update, delete chapters with timestamps |
| Subtitles | Upload subtitles per language; multi-format support via `mantas-done/subtitles` |
| End-screen layers | Custom overlay cards at end of video (VideoMeta "layers") |
| Custom meta | Arbitrary key/value meta storage per video |

### 4.4 Channel

| Feature | Details |
|---------|---------|
| Channel model | One channel per publisher; auto-created on first video |
| Channel statuses | `draft`, `published`, `freeze` (mutes owner) |
| Subscribe / Unsubscribe | Authenticated users |
| Publisher update | Edit channel name, avatar, banner, description |
| Statistics | Daily, monthly, total views and subscriber stats |
| Performance metrics | Total and monthly performance report |
| YouTube Import | Request import, mark completed, update channel metadata |
| Auto-import toggle | Publisher can enable/disable YouTube auto-sync |
| Admin CRUD | Full channel management including freeze/unfreeze |

### 4.5 Comments

| Feature | Details |
|---------|---------|
| Post comment | Authenticated users (mute-gated) |
| Reply to comment | Nested replies |
| Like / Dislike | Per-comment user relation |
| Pin / Unpin | Channel owner can pin a comment |
| Delete | Comment owner and admin |
| Report | Authenticated users |
| Publisher inbox | Paginated comment listing for publisher |
| Remember / unremember | Publisher bookmarks comments for follow-up |
| Read/Unread replies | Toggle read state; mark all replies as read |
| Stats | Comment counts for publisher dashboard |

### 4.6 Playlists

| Feature | Details |
|---------|---------|
| CRUD | Authenticated users create/edit/delete playlists |
| Add/Remove video | Single and bulk operations |
| Public playlists | Viewable by anyone via hash |
| Channel playlists | Listed on channel page |

### 4.7 Search

- Searches video **title**, **description**, and matched **tags** (≥ 3 chars)
- Searches channels by **owner name** and **channel name**
- Filters: `time` period, `media_type` (video / podcast)
- Results include both videos and channels

### 4.8 Notifications

| Feature | Details |
|---------|---------|
| Real-time | Pushed via Laravel WebSockets + Pusher |
| Scopes | Separate notifications for `user`, `publisher`, `admin` |
| Mark as read | Single notification or mark all as read |
| Unread count | Per-scope unread count endpoint |
| Admin broadcast | Admin can send notifications to all users or all publishers |
| Admin management | Create, view, soft-delete, restore notifications |

### 4.9 Monetisation & Earnings

| Feature | Details |
|---------|---------|
| Monthly earnings calculation | Admin triggers calculation; distributes monthly budget among qualified publishers |
| Qualified status | Channels must meet criteria to qualify for monetisation |
| Budget management | Admin sets monthly distribution budget |
| Earnings listing | Publisher sees own earnings; admin sees all |
| Mark as paid | Admin marks earnings paid; creates transaction record |
| Payout records | Separate payout model with detailed history |
| PDF export | Per-earning PDF for publisher; bulk CSV export for admin |
| Total distributed money | Tracked and settable by admin |
| Publisher performance | Total and monthly performance overview |
| Admin export | Publisher earnings export to CSV |

### 4.10 Payments & Subscriptions

| Feature | Details |
|---------|---------|
| Stripe | Setup intent, card subscription, Stripe Checkout |
| Coinbase Commerce | Crypto payment with webhook handler |
| Plans | Admin-managed tiered plans |
| Pricing | Linked to plans; supports multiple payment methods |
| Hero Membership | Subscription-based membership tiers |
| NFT Membership | TC Polygon NFT transfer webhook updates hero status automatically |
| Transactions | Full transaction ledger (admin view) |

### 4.11 Publisher Payment Details

| Feature | Details |
|---------|---------|
| Payout address | Publisher registers ETH wallet or other payout address |
| Verification | Payment details verification step |
| Address history | Full history of submitted addresses |
| Admin controls | View, archive, change status of payment details |

### 4.12 Referral Programme

| Feature | Details |
|---------|---------|
| Referral code | Unique code per user; check availability |
| Referral points | Tracked as monetise points |
| Activate points | Publisher converts referral points to active |
| Statistics | Daily and monthly referral statistics |

### 4.13 TCG Token System

| Feature | Details |
|---------|---------|
| Total supply | 3,500,000,000 TCG tokens |
| Distribution | Points awarded for watch activity (MongoDB-backed) |
| Daily watch limit | Per-user daily earning cap (Redis-cached flag) |
| Locked tokens | Tokens with future `activate_at` date |
| Token history | Full transaction history per user |
| Admin dashboard | Token distribution overview, daily/monthly statistics |

### 4.14 Cryptocurrency & Market

| Feature | Details |
|---------|---------|
| Cryptocurrency listing | Public market data listing |
| Historical prices | Time-series price data per coin |
| Favourite coins | Authenticated users add/remove favourites |
| Crypto campaigns | Admin creates campaigns linking content to specific coins |
| Buy-click tracking | Tracks user buy-intent clicks on coin campaigns |
| Campaign statistics | View and export campaign click statistics |

### 4.15 Advertising

| Feature | Details |
|---------|---------|
| Ad campaigns | Admin CRUD; linked to companies |
| Ad tiers | Tiered slot pricing |
| Slot management | Check filled slots; price per slot per date |
| Discounts | Discount rules for ad slots |
| Ad settings | Configurable ad system settings |
| Ad spaces | Named ad space configuration (options system) |
| Banner ads | Banner ad type campaigns |
| Buy buttons | Buy-button ad type campaigns |

### 4.16 Lottery

- Public lottery listing
- Admin can run a lottery draw (select winners)
- Admin marks lottery prize as paid
- Linked to platform point/token system

### 4.17 Support Messaging

- Authenticated publishers and Hero members can create support messages
- Reply threading (user ↔ admin)
- Mark as seen / close ticket
- Admin full inbox management

### 4.18 Content Management

- Static content pages (CMS-lite) — admin CRUD, public read
- FAQ management (admin)
- Feedback form (public submit; admin view with location data)
- Mail list / newsletter subscription (public subscribe; admin view)
- Forbidden words list (admin-configurable)
- Report reasons configuration (admin)

### 4.19 Access Control

| Role | Capabilities |
|------|-------------|
| `user` | Watch, like, comment, subscribe, playlist, bookmark, report |
| `publisher` | All user + upload videos, manage channel, view earnings, request payouts |
| `admin` | Full access to all resources; management, configuration, reporting |

Additional middleware:
- `user.unmute` — blocks muted users from posting
- `channel.unfreeze` — blocks publishers of frozen channels from creating content
- `access.check:publisher,hero` — restricts to publishers and Hero members
- `2fa` / `2fa:hard` — requires 2FA on sensitive actions
- `waf.ratelimit` — WAF-based rate limiting
- `waf.validate-hash` — validates request integrity

### 4.20 Real-time Events (Pusher/WebSockets)

| Event | Trigger |
|-------|---------|
| `VideoCreated` | New video published |
| `VideoUpdated` | Video edited |
| `VideoDeleted` | Video removed |
| `VideoViewed` | Video view incremented |
| `VideoWatched` | Watch-time stored |
| `VideoWasHidden` / `Unhidden` | Admin hides/restores video |
| `VideoLiked` | Video liked |
| `VideoCommented` | New comment posted |
| `CommentLiked` | Comment liked |
| `ChannelSubscribed` | Channel subscription event |
| `ChannelUpdated` | Channel profile updated |
| `ChannelImportRequestCreated/Accepted/Completed` | YouTube import lifecycle |
| `NewPublisherRequested` | Publisher application submitted |
| `PublisherRequestApproved/Rejected` | Publisher application decision |
| `MessageCreatedByAdmin/User` | New support message |
| `MessageRepliedByAdmin/User` | Support message reply |
| `UserVerified` | Email verification completed |
| `Market` | Market data update |

---

## 5. Publisher & Admin Panel (`tc-publisher-panel`)

A separate React SPA served at its own domain/port. It contains two distinct apps: the **Publisher** dashboard and the **Admin** back-office.

### 5.1 Publisher Dashboard

#### Authentication
- Email/password login
- Password reset
- Email verification
- Publisher-scoped Passport token

#### Dashboard
- Overview: video count, subscriber count, total views, total watch time
- Chart: views and watch-time trends (daily/monthly)
- Quick links to key sections

#### Video Management
- **Video list** — searchable/filterable table of all videos
- **Upload** — direct S3/R2 multipart pre-signed URL upload
- **Studio view** — detailed per-video editing workspace:
  - Title, description, category, tags, language, thumbnail
  - Cryptocurrency associations
  - Chapter management (add/edit/delete with timestamps)
  - Subtitle upload (multi-language)
  - End-screen overlay layer configuration
  - Publish / unpublish / archive
- **Video overview** — analytics summary per video
- **Bulk delete** videos

#### Video Statistics
- Per-video: daily, monthly, total views/watch-time
- Channel-wide: daily, monthly, total performance

#### Channel Management
- Edit channel name, avatar, banner, description
- View channel status (draft / published / frozen)
- YouTube import request submission
- YouTube auto-import toggle
- YouTube sync request

#### Comment Management
- Full comment inbox
- Mark as read / unread
- Remember (flag) / unremember comments
- Mark all replies as read
- Comment stats (total, unread)

#### Playlist Management
- Create, edit, delete playlists
- Add / remove videos from playlists

#### Monetisation
- Earnings overview (monthly earnings list)
- Total earnings (summary)
- Monthly breakdown chart
- Qualified status indicator
- Payout listing
- Export earnings as PDF (per month)

#### Payment Details
- Register payout wallet address (ETH or other)
- Verify payment details
- View address history

#### Notifications
- Publisher notification inbox
- Mark as read (single / all)

#### Score Board
- Publisher ranking/leaderboard

#### Invite & Earn (Referral)
- Referral link generation
- Referral statistics (daily / monthly)
- Activate referral points

#### TCG Token Page
- Token balance overview
- Locked vs unlocked tokens
- Daily watch limit status

#### Support
- Create support message tickets
- View message thread history

#### Profile
- Edit publisher profile details

#### Publisher Application
- Publisher request form (for non-publisher users)
- Publisher terms acceptance

#### Import Request
- Submit YouTube channel import request

---

### 5.2 Admin Panel

Full platform administration back-office.

#### Dashboard
- Platform-wide overview: users, channels, videos, earnings
- Key metrics at a glance

#### User Management
- List all users with search/filter
- View user detail
- Create new users / admins
- Edit user data
- Soft-delete and restore users
- Manage publisher requests (approve / reject)

#### Channel Management
- List all channels
- View / edit channel details
- Freeze / unfreeze channels
- Delete channels
- View deleted channels (restore)
- Per-channel statistics (daily / monthly / total)
- YouTube import management (view requests, mark completed)
- Update YouTube import channel metadata

#### Video Management
- List all videos (all publishers)
- Create / delete videos
- Hide / unhide videos (soft moderation)
- Bulk-assign category to multiple videos
- YouTube Importer: add videos via YouTube URL
- Per-video statistics

#### Categories
- Create, update, delete categories
- Public: list and view

#### Tags
- Create, update, delete, list tags
- Public: list tags

#### Earnings Management
- List all publisher earnings
- View monthly earnings totals
- Set total distributed money budget
- Trigger earnings calculation
- Mark earnings as paid (creates transaction)
- CSV export of earnings

#### Monetisation Management
- View qualified channels
- Set/get monthly budget
- View all payouts
- Mark payouts as paid
- Export monetisation payouts as CSV

#### Payments & Transactions
- Transaction ledger (all users)
- Membership subscriber list
- Membership earnings (daily / monthly / total)
- Payment details management (view, archive, change status)

#### Plans
- Create, update, delete, list membership plans

#### Ads Manager
- **Campaigns** — full CRUD; linked to companies
- **Banner Ads** — banner campaign management
- **Buy Buttons** — buy-button campaign management
- **Settings** — ad system configuration
- Check filled slots by tier/date
- Price-per-slot by tier and date
- Discount management

#### Lottery
- View lottery history
- Run a lottery draw
- Mark prize as paid

#### CRM
- Customer relationship management section

#### Crypto Currencies
- Cryptocurrency data management
- Campaign-linked coin listing

#### Reports
- Video reports listing (per video report breakdown)
- Comment reports listing (per comment report breakdown)

#### Feedbacks
- User feedback listing with location data

#### Notifications
- Send notifications to all users or all publishers
- View sent-by-admin notification history
- Delete / restore notifications

#### Messages (Support)
- Full support message inbox (all users)
- Reply to messages
- Mark as seen / close tickets

#### Emails List
- Newsletter / mail list subscriber management with location data

#### FAQ
- Create, update, delete FAQ entries

#### TCG Token Dashboard
- Total distributed tokens
- Daily / monthly distribution statistics
- Token history per user

#### Logs
- System / access log viewer

#### Settings
- System-wide configuration options
- Forbidden words list
- Report reasons configuration
- TCG circulation supply
- Ad space configuration

---

## 6. Cross-Cutting Features

### Known Gaps & Dead Routes

The following features have code/components but are **not wired into routing** or are stubs:

| Item | Status |
|------|--------|
| `/membership/membership` (web app) | Returns `null` — disabled stub |
| `/me/messages` (web app) | Route does not exist; `oldMessages` create flow redirects here incorrectly |
| `podcasts` page | Requires authentication (`guard: true`) — unauthenticated users hit `/403` |
| Publisher scoreboard page | Code exists (`score-board/`) but **no route** in `PublisherApp.js` |
| Publisher support ticketing (full page) | Code exists but **no route**; only the FAQ page is wired at `/publisher/faq` |
| Publisher full notifications page | Not routed; only the navbar popover functions |
| Channel name change | Links to `/publisher/tickets/create/change-channel-name-request` — **no matching route** |
| Live streaming | No routes, models, or ingest pipeline exist in any of the three parts |
| Shorts / vertical video format | Not implemented; only `video` and `podcast` media types exist |
| i18n / localisation | No i18n framework; UI is English-only (subtitle metadata is multi-language) |

---

### Multi-language Support
- Languages listed via API
- Videos tagged with a language
- Subtitles stored per language code
- Frontend supports multiple display languages

### Responsive Design
- Web app has dedicated mobile and desktop component trees
- Touch-optimised UI for mobile users

### SEO
- Next.js SSR/SSG for indexable video and channel pages
- React Helmet for meta tags
- Dynamic OG tags per video

### Caching Strategy
- Redis caches home page data (trending videos, top channels) for 1 hour
- Laravel Passport tokens cached in Redis
- WAF rate-limiting state in Redis

### Security Layers
- WAF rate limiting (configurable per endpoint)
- Suspicious IP tracking and blocking
- Mute system (user-level and channel-level)
- Captcha for sensitive forms
- 2FA gate for account mutations
- Email verification gate for account deletion
- Hash validation on view increment endpoints

### Content Moderation
- Video hide/unhide (admin)
- Channel freeze (auto-mutes channel owner)
- Comment pin/unpin by channel owner
- User mute (blocks posting)
- Report system (videos and comments)
- Admin report review

### PDF & Export
- Publisher earnings: per-month PDF download
- Monetisation payouts: CSV export
- Publisher earnings: CSV export for admin

### Crypto / Web3 Integration
- Ethereum wallet login and registration
- NFT-based Hero membership (TC Polygon)
- ETH wallet address on publisher profile (payout)
- Crypto buy-button ad campaigns
- Favourite cryptocurrencies tied to personalised content feed

---

## 7. API Endpoint Reference

### Public Endpoints (No Auth)

```
GET    /api/home
GET    /api/home/channels/trending
GET    /api/home/channels/top
GET    /api/home/videos/trending
GET    /api/home/videos/for-you
GET    /api/search/{keyword}
GET    /api/videos
GET    /api/videos/{id_or_url_hash}
GET    /api/videos/{id_or_url_hash}/related
GET    /api/videos/{id_or_url_hash}/chapters
GET    /api/videos/{id_or_url_hash}/subtitles
GET    /api/videos/{id_or_url_hash}/layers
GET    /api/videos/{id_or_url_hash}/meta
GET    /api/videos/{id_or_url_hash}/meta/{key}
PUT    /api/videos/{id}/increase_view
POST   /api/videos/{id}/watch
GET    /api/channels
GET    /api/channels/{id_or_slug}
GET    /api/channels/{id}/playlists
GET    /api/playlists/{id}
GET    /api/categories
GET    /api/categories/{id}
GET    /api/tags
GET    /api/tokens
GET    /api/market/cryptocurrencies
GET    /api/cryptocurrencies
GET    /api/cryptocurrencies/{slug}/historical-price
PUT    /api/cryptocurrencies/{id}/buy/{campaign}
GET    /api/lotteries
GET    /api/plans
GET    /api/payment-methods
GET    /api/languages
GET    /api/contents/{id}
GET    /api/options/reasons/{key}
GET    /api/options/forbidden-words
GET    /api/options/ad-spaces
GET    /api/options/tcg-circulation-supply
GET    /api/videos/{id}/comments
GET    /api/comments/{id}
POST   /api/register
POST   /api/login
POST   /api/login/{admin|publisher}
POST   /api/login/magic/{scope}
POST   /api/wallet/login
POST   /api/wallet/register
GET    /api/wallet/get-message
POST   /api/password/send
GET    /api/password/verify/{token}
PUT    /api/password/reset
POST   /api/feedback
POST   /api/mail-list
POST   /api/inquire
GET    /api/captcha
POST   /api/captcha
POST   /api/identify/webhook-handler
POST   /api/coinbase/webhook-handler
POST   /api/tc-polygon/update-hero-data
```

### Authenticated User Endpoints

```
GET    /api/logout
GET    /api/profile
POST   /api/profile
DELETE /api/profile
POST   /api/profile/password
GET    /api/profile/2fa
GET    /api/profile/membership-data
GET    /api/profile/security-data
GET    /api/profile/custom-feed
POST   /api/profile/custom-feed
POST   /api/profile/eth-address
POST   /api/profile/wallet-address
POST   /api/profile/login-type
DELETE /api/account/delete
GET    /api/account/restore/{token}
GET    /api/subscribed-channels
PUT    /api/channels/{id}/subscription
PUT    /api/videos/{id}/like
PUT    /api/videos/{id}/dislike
GET    /api/videos/bookmarks
PUT    /api/videos/{id}/bookmark
GET    /api/videos/subscribed-channels
PUT    /api/playlists/{id}/add/{video}
PUT    /api/playlists/{id}/remove/{video}
PUT    /api/playlist/add
PUT    /api/playlist/remove
POST   /api/playlists
PUT    /api/playlists/{id}
DELETE /api/playlists/{id}
GET    /api/my-playlists
POST   /api/videos/{id}/comments
POST   /api/comments/{id}/reply
PUT    /api/comments/{id}/like
PUT    /api/comments/{id}/dislike
PUT    /api/comments/{id}/pin
PUT    /api/comments/{id}/unpin
DELETE /api/comments/{id}
POST   /api/videos/{id}/report
POST   /api/comments/{id}/report
GET    /api/notifications
GET    /api/notifications/{id}
GET    /api/notifications/{scope}/count
PUT    /api/notifications/{scope}/read
PUT    /api/notifications/{id}/read
GET    /api/cryptocurrencies/favorites
PUT    /api/cryptocurrencies/{id}/add-to-fav
PUT    /api/cryptocurrencies/{id}/remove-from-fav
GET    /api/channel/performance/total
GET    /api/channel/performance/monthly
PUT    /api/videos/{id}/increase-share-link-count
GET    /api/share-links/videos
GET    /api/share-links/statistics
PUT    /api/2fa/email/enable
PUT    /api/2fa/email/disable
PUT    /api/2fa/google/qr-code
PUT    /api/2fa/google/enable
PUT    /api/2fa/google/disable
PUT    /api/2fa/verify
PUT    /api/2fa/email/send
POST   /api/publisher/apply
POST   /api/messages
POST   /api/messages/{id}/reply
PUT    /api/messages/{id}/seen
PUT    /api/messages/{id}/close
POST   /api/pricing/{id}
POST   /api/pricing/{id}/process
GET    /api/profile/pricing
GET    /api/stripe/setup-intent
DELETE /api/stripe/subscription/cancel
GET    /api/identify/verification-url
POST   /api/upload
```

### Publisher Endpoints (`/api/publisher/*`)

```
GET    /api/publisher/dashboard/overview
GET    /api/publisher/dashboard/charts
GET    /api/publisher/score_board
GET/POST/PUT/DELETE /api/publisher/videos
PUT    /api/publisher/videos/{id}/status/published
DELETE /api/publisher/videos (bulk)
POST   /api/publisher/videos/bulk-pin
POST   /api/publisher/videos/{id}/layers
POST   /api/publisher/videos/{id}/meta/{key}
POST   /api/publisher/videos/{id}/subtitles
DELETE /api/publisher/subtitles/{id}
POST/PUT/DELETE /api/publisher/videos/{id}/chapters
GET    /api/publisher/videos/{id}/statistics
GET    /api/publisher/videos/{id}/statistics/daily
GET    /api/publisher/videos/{id}/statistics/monthly
GET    /api/publisher/videos/{id}/statistics/total
GET    /api/publisher/channel
PUT    /api/publisher/channel
GET    /api/publisher/channel/statistics
GET    /api/publisher/channel/statistics/daily
GET    /api/publisher/channel/statistics/monthly
GET    /api/publisher/channel/statistics/total
POST   /api/publisher/channels/request-import
PUT    /api/publisher/yi/channels/sync-request
PUT    /api/publisher/yi/channels/auto-import
GET    /api/publisher/yi/channels/import-stats
GET    /api/publisher/comments/stats
GET    /api/publisher/comments
DELETE /api/publisher/comments/unremember-all
PUT    /api/publisher/comments/{id}/remember
PUT    /api/publisher/comments/{id}/toggle-read
PUT    /api/publisher/comments/read-all-replies
GET    /api/publisher/notifications
GET    /api/publisher/earnings
GET    /api/publisher/earnings/total
GET    /api/publisher/earnings/monthly
GET    /api/publisher/earnings/total-distributed-money
GET    /api/publisher/earnings/{id}/export-as-pdf
GET    /api/publisher/monetization/payouts
GET    /api/publisher/monetization/qualified-status
GET    /api/publisher/monetization/current-month-budget
GET    /api/publisher/monetization/payouts/export/pdf
POST   /api/publisher/profile/payment-details
POST   /api/publisher/profile/payment-details/verify
POST   /api/publisher/profile/eth-address
GET    /api/publisher/profile/address-history
POST   /api/publisher/monetize/active-referral-points
GET    /api/publisher/monetize/referral-statistics
DELETE /api/publisher/account/delete
GET    /api/publisher/s3/pre-signed-url-for-upload-video
GET    /api/publisher/r2/pre-signed-url-for-upload-video
GET    /api/publisher/upload/pre-signed-url-for-upload-video
```

### Admin Endpoints (`/api/admin/*`)

```
GET    /api/admin/dashboard
GET    /api/admin/users
GET    /api/admin/users/{id}
POST   /api/admin/users
PUT    /api/admin/users/{id}
DELETE /api/admin/users/{id}
PUT    /api/admin/users/{id}/restore
GET    /api/admin/publishers
GET    /api/admin/admins
POST   /api/admin/admins
GET    /api/admin/publisher-requests
PUT    /api/admin/publisher-requests/{id}/confirm
PUT    /api/admin/publisher-requests/{id}/reject
GET    /api/admin/channels
GET/PUT/DELETE /api/admin/channels/{id}
POST   /api/admin/channels
GET    /api/admin/channels/{id}/statistics (daily/monthly/total)
GET    /api/admin/channels/import-requests
POST   /api/admin/channels/{id}/import-completed
PUT    /api/admin/channels/{id}/import-request
PUT    /api/admin/yi/channels/{id}
GET    /api/admin/users/{id}/performance/total
GET    /api/admin/users/{id}/performance/monthly
GET    /api/admin/videos
POST   /api/admin/videos
GET    /api/admin/videos/{id}
DELETE /api/admin/videos/{id}
PUT    /api/admin/videos/{id}/hide
PUT    /api/admin/videos/{id}/unhide
PUT    /api/admin/videos/bulk-assign-category
POST   /api/admin/yi/videos
GET    /api/admin/videos/{id}/statistics (daily/monthly/total)
GET    /api/admin/comments
DELETE /api/admin/comments/{id}
GET    /api/admin/earnings (total/monthly)
PUT    /api/admin/earnings/total-distributed-money
POST   /api/admin/earnings/calc
PUT    /api/admin/earnings/{id}/paid
GET    /api/admin/monetization/qualified-channels
GET    /api/admin/monetization/payouts
PUT    /api/admin/monetization/budget
GET    /api/admin/monetization/budget
PUT    /api/admin/monetization/payouts/mark-as-paid
GET    /api/admin/monetization/payouts/export/csv
GET    /api/admin/transactions
GET    /api/admin/memberships
GET    /api/admin/membership/earnings/daily
GET    /api/admin/membership/earnings/monthly
GET    /api/admin/membership/earnings/total
GET/POST/PUT/DELETE /api/admin/plans
GET    /api/admin/payment-methods
GET/POST /api/admin/payment-details
POST   /api/admin/users/{id}/payment-details
POST   /api/admin/payment-details/change-status
POST   /api/admin/payment-details/mark-as-archive
POST   /api/admin/payment-details/mark-as-non-archive
GET    /api/admin/payment-details/{id}
GET    /api/admin/channels/{id}/address-history
GET/POST/PUT/DELETE /api/admin/categories
GET/POST/PUT/DELETE /api/admin/tags
GET/POST/PUT/DELETE /api/admin/contents
GET/POST/PUT/DELETE /api/admin/companies
GET    /api/admin/roles
GET/POST/PUT/DELETE /api/admin/crypto-campaigns
GET    /api/admin/crypto-campaigns/{id}/statistics
GET    /api/admin/ads/campaigns
POST   /api/admin/ads/campaigns
PUT    /api/admin/ads/campaigns/{id}
DELETE /api/admin/ads/campaigns/{id}
GET    /api/admin/ads/campaigns/{id}
GET    /api/admin/ads/discounts
GET    /api/admin/ads/settings
PUT    /api/admin/ads/settings
GET    /api/admin/ads/price/{tier}/{date}
GET    /api/admin/ads/filled-slots
GET    /api/admin/lotteries
POST   /api/admin/lotteries
PUT    /api/admin/lotteries/{id}/paid
GET    /api/admin/notifications
GET    /api/admin/notifications/sent-by-admin
POST   /api/admin/notifications/publisher
POST   /api/admin/notifications/user
GET    /api/admin/notifications/{id}
DELETE /api/admin/notifications/{id}
PUT    /api/admin/notifications/{id}/restore
GET    /api/admin/messages
POST   /api/admin/messages
POST   /api/admin/messages/{id}/reply
PUT    /api/admin/messages/{id}/seen
PUT    /api/admin/messages/{id}/close
DELETE /api/admin/messages/{id}
GET    /api/admin/reports/video
GET    /api/admin/reports/comment
GET    /api/admin/reports/video/{id}
GET    /api/admin/reports/comment/{id}
GET    /api/admin/feedback
GET    /api/admin/feedback/locations
GET    /api/admin/mail-list
GET    /api/admin/mail-list/locations
GET    /api/admin/tokens/dashboard
GET    /api/admin/tokens/history
GET    /api/admin/cryptocurrencies (relatedto-campaigns)
GET    /api/admin/channels/statistics/daily
GET    /api/admin/channels/statistics/monthly
GET    /api/admin/channels/statistics/total
GET    /api/admin/users/publishers-earnings/export
GET    /api/admin/playlists
POST   /api/admin/playlists
POST   /api/admin/options/reasons/{key}
GET    /api/admin/options/reasons/{key}
POST   /api/admin/options/forbidden-words
POST   /api/admin/options/tcg-circulation-supply
GET    /api/admin/options/ad-spaces
POST   /api/admin/options/ad-spaces
GET    /api/admin/security-rate-limit/report
GET    /api/admin/channels/{id}/playlists
```

---

*Generated by automated codebase analysis — May 2026*
