---
created: 2026-10-24
---
# Case Study Stories (English, Humanized)

All three English stories in one note, edited for plain wording before they go on amiryousefi.com. This version includes the second edit with Amir's decisions (Oct 24, 2026). The changes and the facts to check are in [[Story Humanization Review]].

Originals: [[Today's Crypto Story (English)]] · [[SaymanDigital Story (English)]] · [[Asr'e Ahan Story (English)]]

Contents:
- [[#Today's Crypto]]
- [[#Sayman Digital]]
- [[#Asr'e Ahan]]

---

## Today's Crypto

Original note: [[Today's Crypto Story (English)]]

Part of [[Todays Crypto Case Study]]. English version of [[Today's Crypto Story (Farsi)]].

> [!info] At a glance
> - **Client:** Today's Crypto (TC), a Swedish startup building a video platform for the crypto community, backed by the founder's company, EQ Gruppen
> - **Role:** CTO, from December 2020 to early 2025. I came in to rebuild a failing codebase and stayed to own architecture, team, delivery and production
> - **Team:** four core engineers (me, frontend, backend, panels), later joined by a smart-contract engineer and a UI developer. On the client side: the founder/CEO, a QA and product owner, and a partnerships lead
> - **What we built:** a three-part platform (Next.js viewer app, React publisher and admin panel, Laravel API), a Python YouTube importer, a Node.js blockchain integration service, and the TCG token contracts on Polygon
> - **Web3 layer:** wallet login, the TCG ERC-20 governance token (5 billion fixed supply), watch-to-earn rewards with on-chain claims, vesting wallets, NFT-based HODL memberships, and crypto payments
> - **Milestones:** closed beta on 9 May 2021 · public publisher launch August-September 2022 · desktop launch December 2022 · TCG live on Polygon mid-2023 · first community airdrop in November 2023, with **2,000+ signups on day one** and peak traffic of **up to 20,000 real unique visitors a day**, on top of a much larger wave of farming bots

---

### Who the client was

Today's Crypto was the idea of a Swedish entrepreneur who already ran an established consumer-products company, EQ Gruppen. The pitch was simple: a YouTube for crypto. Crypto creators were posting on general-purpose platforms that did not care about their niche. Their audience lived in wallets, tokens and price charts. They should have a home built for them.

Simple to say, hard to build. A video platform on its own is already a big product: upload, transcode, watch, subscribe, comment, recommend, monetise. This one also had to feel native to crypto users, which meant wallet login, live market data, a token economy and on-chain ownership.

The founder had business experience and a strong product sense. What he did not have was a working codebase or a technical team.

### How I came in

In November 2020 I was introduced to the founder through Proxify, a Stockholm-based network that matches vetted developers with companies. The first call was on 12 November 2020.

The project was not starting from zero. It was starting from somewhere worse. A previous developer had built a first version, and his own handover notes, sent to the client and me the same day, were blunt about it: *"the whole script is bad and I think this script is not intended for modification by other developers."* No autoloading, no package manager, no MVC, routing through `.htaccess`, PHP and JavaScript mixed in the same files.

The founder's reaction was the right one: *"If there is that much code that needs to be replaced, we need to look into this and see if it's worth the time."*

It was not. I recommended a rebuild, and we started one. By **30 December 2020** the first deployed version of the new platform was running, with home, category, video and channel pages, subscribe, likes and bookmarks. Signup and login followed two weeks later.

From that point I was no longer the developer on the project. I was the person responsible for the technology side of the company, and formally its CTO.

### Rebuild, not repair: the architecture

The early decisions carried the product for years, so I want to be precise about them.

**Three surfaces, one API.** A Next.js web app for viewers, a single React application for both publishers and admins, and a Laravel API behind both. Viewer work, creator tooling and back-office features could each ship on their own schedule without blocking each other.

**Server-side rendering for discovery.** A media platform that search engines cannot read has no organic reach. We picked Next.js with SSR for SEO, not fashion.

**Mobile first, literally.** The crypto audience is on phones. For most of 2021 the product *was* the mobile web app (internally "MWA"), with separate mobile and desktop component trees per page. The desktop web app came later, launched in December 2022.

**Split data by access pattern.** Business records in MySQL. Watch time, token points and channel statistics in MongoDB. Write-heavy behavioural data does not belong in the same store as users and payments, and that separation later made the token system possible.

**Media off the application servers.** Video moved to object storage, first S3 and then Cloudflare R2, uploaded directly from the browser with pre-signed URLs, so large uploads never passed through the API.

**Three environments from the start.** `beta` for daily integration, `cl-beta` for the closed-beta users and the founder's testing, and production. That discipline later let a small team deploy several times a week without breaking what testers were using.

### Building the team

I started alone. In January 2021 I brought in the first engineer, a frontend developer I trusted, at the same rate as mine. By mid-2021 a backend engineer and a second frontend engineer, who would own the publisher and admin panels, had joined. That team of four built the core of the platform and stayed together for most of the next four years.

The team later expanded for specific needs: a smart-contract engineer for the token work in 2023, and a UI developer in 2024. When we needed a small, self-contained tool in 2021, I brought in a contractor from my network on a fixed budget rather than growing headcount. The founder added a bonus if it shipped, integration included, before a set deadline.

On the client side the team grew too: a product and QA owner who tested every ticket before release, and a partnerships lead who signed creator channels.

### The working rhythm

We were a distributed team working with a founder in another country and another time zone. We kept the mechanics that made that work deliberately simple.

- **Regular syncs** with the founder at a fixed time, 10:00 CET (our late morning), plus Loom walkthroughs and voice notes when a meeting did not fit.
- **The founder as the first real user.** Every build went to him on his own phone. When an iOS-only bug showed up that we could not reproduce, we added BrowserStack so we could test on the same devices our users had.
- **A shared board.** Trello from July 2021, then Jira with separate projects for the 1.0 platform, the ongoing improvement track, and the TCG token integration. Tickets moved through *Backlog → Selected for Development → Business QA → Ready for deployment → Done*, so nothing reached production without passing the client's own QA.
- **Sprint planning with the client.** The founder and the product owner set priorities. I turned them into child issues, estimated them with the team, and briefed each developer.
- **Radical time transparency.** From May 2022 every developer kept a daily log, with hours and what was done, in a report the client could open at any time. Invoices matched those logs.

That last point matters more than it looks. A startup that is bleeding money needs to see where it is going. Nobody on the client side ever had to wonder what the team did last week.

### Closed beta: May 2021

Five months after the rebuild started, on the night of **9 May 2021**, I wrote to the founder at two in the morning: *"WE ARE UP."* The closed beta went live with imported videos from the first two channels, sorted into BTC, ETH, altcoins and DeFi categories.

What followed was the normal, unglamorous part: fixing a related-video playback bug, a drawer that rendered wrong on some iPhones, avatar uploads from the camera, font sizes. Then we restructured the video page, the core page of the product, for speed, and rolled that pattern out to the rest of the app.

Over the rest of 2021 the product started to look like itself:

- A live **coin ticker** under each video and a **market drawer** on every page, ranked by market cap. The founder's comment when he saw it: *"Now I don't need CoinMarketCap anymore."*
- **Coin pages** with detailed market data from the CoinMarketCap API
- **Video chapters** and a custom player with tap-to-unmute and a minimised mode
- **Real-time notifications** across all three surfaces
- **Stripe** subscriptions

### From beta to a real platform: 2022

2022 was the year the platform had to become something the company could put in front of real creators and real users, and then in front of investors.

The work that year was mostly trust infrastructure:

- **Two-factor authentication** by email code and by authenticator app (TOTP with QR code), with a hard 2FA gate on sensitive actions
- **KYC with iDenfy** for publishers, so creators could be paid correctly and legally, with every change to payment details logged
- **Six-digit email verification** instead of activation links
- A full **comment manager** for publishers: read/unread, mentions, pinning, follow-up flags
- **Chromecast and AirPlay** casting in the video player
- Landing pages for users and publishers, launched publicly in August 2022

In September 2022 the founder sent the team a letter. The company had been *"bleeding since we started this project,"* it now had software *"so good that we feel confident inviting real users and content creators to it,"* and it needed real user data to raise more money. The development budget was cut, temporarily.

That changed what "most important" meant. The biggest barrier to growth was content, and no established creator was going to re-upload their whole library to a new platform. So we built a **YouTube importer**. A publisher connects their channel, and the importer pulls the back catalogue and keeps syncing new uploads, with titles, descriptions, thumbnails and chapters.

The first real creator channel was imported overnight in September 2022, about a hundred videos by morning. Brand channels followed, including CoinGecko and OKX, and over the next year more than a dozen crypto channels were onboarded. The desktop web app launched in December 2022.

### The Web3 layer and the TCG token

This is the part that made the platform Today's *Crypto* instead of another video site. It is also the part with the least room for error. On-chain mistakes cannot be rolled back.

#### What users saw

- **Wallet login and registration.** MetaMask and WalletConnect through Web3Modal and wagmi, next to email/password and passwordless magic links. The backend verifies wallet ownership with a signed message (Keccak-256 signature recovery), so a user can create an account with nothing but a wallet.
- **Watch-to-earn.** Users earn TCG for engaging with the platform: 1 TCG per minute watched, 25 TCG for setting up a custom feed, 5 TCG per invited friend. They earn from the moment they sign up, with no wallet needed until they want to claim. There was no token sale. Tokens were meant for the people using the platform.
- **Claiming on-chain.** Earned tokens start as locked. Once they unlock, a user with at least 500 TCG connects their wallet and claims them to Polygon from the TCG page, which shows claimable, locked and total balances plus claim history.
- **HODL memberships as NFTs.** Two NFT editions minted on Polygon. The White edition (50 MATIC, capped at 100k) earns 1-3 TCG per minute watched, up to 180 a day. The Black edition (250 MATIC, capped at 20k) earns 5-15 per minute, up to 900 a day, and removes ads. The platform listens for NFT transfers and updates a user's membership status automatically when the NFT moves wallets.
- **Crypto payments.** Coinbase Commerce checkout next to Stripe. The simplified 2023 plans were $5 a month or $50 a year, with 5,000 TCG included in the yearly plan.
- **Governance and transparency.** A governance page describing TCG holders voting on content quality and new features, with voting power snapshotted before each proposal and 10% of platform revenue going to a reward pool for voters. A transparency tab listed every contract address and wallet so anyone could verify them on Polygonscan.
- **Crypto-native monetisation.** Publishers register a payout wallet, verified behind KYC and 2FA. Crypto brands run buy-button campaigns tied to specific coins. A "Cha-Ching" share card lets users post their earnings to social media.

![[Attachments/TodaysCrypto/ScreenShots/Web App/Token Earnings.png|700]]

#### The smart contracts

The contracts live in the `TodaysCrypto/Contracts` repository. They are written in Solidity 0.8.9 on OpenZeppelin 4.8, built and tested with Hardhat, linted with solhint, and deployed to Polygon (Mumbai testnet first, then mainnet) through Infura, with source verified on Polygonscan.

| Contract | What it does |
|---|---|
| **`TCGToken`** | ERC-20 token "TodaysCrypto" (TCG), 18 decimals. **5,000,000,000 TCG minted once** at deployment to a distributor address. There is no mint function and burning is disabled, so the supply is fixed forever. Also includes **ERC20Snapshot** (owner-triggered balance snapshots, the basis for snapshot voting and airdrops), **ERC20Votes** (vote delegation and historical voting-power checkpoints for on-chain governance), and **ERC20Permit** (EIP-2612 gasless approvals by signature). |
| **`RewardDistribution`** | The bridge between platform activity and the chain. An account holding `SCRIPT_ROLE`, our backend service, writes batched claimable balances (`updateClaimable(users[], amounts[])`). Users then **pull** their tokens with `claim()`, which zeroes the balance before transferring (checks-effects-interactions). Role-based access control separates the script from the admin. The admin can recover tokens sent to the contract by mistake, but can never withdraw TCG itself. Claims and recoveries emit events. |
| **`TCGVestingWallet`** | OpenZeppelin `VestingWallet`: linear release of allocated tokens to a beneficiary over a set period. The deployment script creates one vesting wallet per allocation (eight in the launch configuration). |

Around the contracts:

- **Deployment scripts** run in order: deploy the token, deploy the reward contract pointing at it, then create the vesting wallets. Addresses are written to a deploy file, so each step uses the last one's output.
- **Tests** cover the full OpenZeppelin ERC-20, snapshot, votes and vesting behaviour suites, plus our own checks: minting and burning must fail, only the script role may update claimable balances, input arrays must match in length, and claims transfer exactly what is owed.
- **Treasury wallets** were set up as **Gnosis Safe multisigs**, so no single key could move company funds.

#### Design choices worth explaining

**Non-upgradeable on purpose.** The token was redeployed to testnet as a version *without* upgradeability before going to mainnet. An upgradeable token lets the team change the rules later. For a token whose value depends on holders trusting a fixed supply, that flexibility is a liability. Fixed code, fixed supply.

**A claimable ledger instead of a Merkle tree.** We first designed claims around a Merkle tree, which is the gas-cheap standard for airdrops. We shipped a simpler model: the backend writes per-user claimable amounts to the contract once a day, and users pull. It costs more gas on our side, paid in MATIC from the script wallet. In exchange every user's balance is readable on-chain, there are no proofs to generate or serve, and above all it creates a **daily control point** between "earned on the platform" and "claimable on-chain." As the next section shows, that control point turned out to be the most important security feature we had.

**Off-chain earning, on-chain settlement.** Watch time, referrals and engagement are tracked off-chain in MongoDB, where writes are free and fast. A Node.js integration service reads settled earnings from the platform API and pushes them to the reward contract at 00:00 GMT each day. Users get a Web2-speed experience, and only actual ownership transfers touch the chain.

![[Attachments/TodaysCrypto/ScreenShots/Web App/Token Governance.png|700]]

### When traffic finally came: the airdrop and the bot farms

On **1 November 2023** the company ran its first community airdrop campaign, ahead of an exchange listing. On paper it worked better than anyone expected. **More than 2,000 users signed up on the first day** and watched more than a thousand videos. The Telegram group turned into what I called a notification bomb. I had to pull over while driving and mute it.

Within hours the platform started going down under the load. Within days we learned that a large share of that traffic was not people.

A token that pays for watch time and referrals is an open invitation to farms. What we saw:

- One referrer with **almost 10,000 referrals** and nearly 100,000 tokens, earned while the referral reward was still higher than the later 5 TCG rate
- About **4,000 registrations in a single day**, a tenth of them through referral links from only about a hundred referrers
- One wallet collecting tokens claimed from many accounts, passing **1.3 million TCG**. At one point that was roughly 10% of everything claimed so far
- A single account sending 2,000 watch-time writes in one day

This is where on-chain design stops being theory. Whatever had already been written to the reward contract could not be taken back. What had not been written yet still could. So the response used the control point we had designed in:

1. **Pause the nightly claimable update** for one night, so no new balances reached the chain while we investigated. The community was told honestly why.
2. **Cut the obvious farms.** We disabled about 80 accounts registered through a temporary-email service, and the referrers behind them.
3. **Add a security layer in front of the API** that logs user ID and IP for every earning request. Within a day it was blocking about **260,000 watch-time writes coming from ~340 IP addresses tied to ~1,270 accounts**.
4. **Revoke off-chain earnings** for accounts that matched farming patterns, such as six accounts on three IPs with the same referrer and nearly identical watch time, before those earnings became claimable.
5. **Harden the front door:** registration limits per IP, two login attempts per minute, captcha, Cloudflare bot protection, and caps on rewards like liked comments that were easy to game.

Then we resumed claims.

At the same time we were keeping the site up. We resized servers, profiled slow MySQL queries, and temporarily switched off server-side rendering so pages could be served faster under load. At peak, Cloudflare showed **up to 20,000 real unique visitors a day**, and the bot traffic farming the token was far larger than that.

Not everything went cleanly, and I would rather say so. One night the distribution wallet ran out of MATIC for gas, so claims stalled. A failed on-chain transaction made users' earned tokens look like they had vanished, and the Telegram group melted down until we traced it. A reward-limit change went live before the previous day's earnings had been made claimable, and it wiped them. We restored them the next morning. Each time, the fix was fast. The lesson was that a token community watches every number in real time, and every operational slip becomes a public trust problem.

### Keeping a startup platform up

For most of its life the platform ran on a very small infrastructure budget, and a lot of my work was keeping it standing.

- **January 2023:** after a server migration, MySQL query logging had been left on and filled the disk. We were down for an hour and a half. The founder asked for an incident log so we would not repeat mistakes. I added a scheduled cleanup, a shared incident log and a **server migration checklist**.
- **February 2023:** outages traced to CPU exhaustion from updating crypto prices every five seconds (slowed to twenty) and to the importer and beta API sharing the production server. We moved the importer and beta onto a separate server so the production API ran alone.
- **Early 2023:** repeated instability at our hosting provider, at the worst possible times, including the evenings when the company had just contacted dozens of US venture capitalists. In **May 2023** I migrated the whole platform to DigitalOcean.
- **November 2023:** a market-data service wrote 59 GB of logs in a few days of airdrop traffic and filled the disk. We disabled it and fixed its logging.

Uptime monitoring ran through Pingdom and edge protection through Cloudflare. Most incidents were fixed within the hour, often late at night. The real weakness was that too many of those fixes depended on one person being reachable. I come back to that below.

### The importer: building on someone else's black box

The YouTube importer was the growth engine, and it was also the platform's most fragile dependency.

YouTube does not want its videos downloaded at scale. Over two years the importer broke because API quotas ran out as we added channels, because the open-source download library stopped working after YouTube changed its data format, because YouTube changed a few meta tags in its HTML, and because storage credentials were revoked. Each time it was fixable: more API keys, automatic restarts when quotas ran out, and eventually a rebuilt importer with more of the pipeline in Python that used far fewer API calls. In September 2023 it ran reliably for weeks, checking every channel every two hours.

But as I told the founder at the time, depending on YouTube was *"like trying to control a black box system."* By late 2024 YouTube was actively blocking this kind of downloading, including from new servers and through proxies, and the importer spent long stretches down. A content platform with stale content is hard to grow, and harder to raise money for.

### What didn't go well

The references I trust most include this section, so here is mine.

**Operations depended too much on me.** Deployments, server access and importer fixes ran through me for too long. When I was sick, which happened more than once in 2023 and 2024, the platform had no real on-call cover, and the founder was left chasing me for updates. It was a common startup pattern: the person who built the system is also its only operator. I should have pushed harder, earlier, for shared runbooks, a second person with production access, and automated alerts instead of the founder noticing that no new videos had arrived.

**Alerting came too late.** The founder asked for importer alerts in February 2023. We built auto-restart in August 2023. That gap cost us weekends of stale content.

**A strategic dependency we could not control.** The importer made onboarding creators easy, and it tied the product's freshness to a platform that did not want us. A plan B, such as creator-side uploads, official partnerships or embedding, should have been a priority, not a someday.

**Budget and morale.** After the 2022 budget cut, the team kept building, and in 2023 delivered the token integration, the migration and the airdrop response. By mid-2024 I told the founder plainly that motivation in the team was very low. By early 2025, with fundraising not closing, the engagement wound down.

### Where it ended

Today's Crypto ran in production from 2021 into 2025: a closed beta, a public platform for creators and viewers, a full Web3 token economy on Polygon, and an airdrop that brought real users along with a lot of bots. It was built and operated by a core team of four engineers and a small client team.

The company did not reach the funding round it was working toward, and the platform is no longer live as Today's Crypto. The core infrastructure we built was preserved and carried into the founder's next venture, which is the most direct evidence I have that the architecture outlived its first product.

### What I take from it

Today's Crypto is the engagement where I learned what it means to be a CTO inside a startup rather than a lead inside a company.

The technical lessons are clear. Rebuild early when the foundation is wrong. Split surfaces and data stores by how they are used. Design token systems so there is always a point between earning and settlement where humans can still intervene. That last one is what saved us when the airdrop brought real users and, with them, the people trying to farm it.

The organisational lessons were harder. In a startup the CTO owns the product *and* the pager, and a system is only as reliable as the least-covered hour of the person running it. Transparency, like daily time logs, a client-run QA stage and an honest incident log, kept a long cross-border relationship healthy through budget cuts, outages and a very public token launch.

If I did it again I would build the same platform. I would build the operating model around it, with shared on-call, automated alerting and a second pair of hands on production, much earlier.


---

## Sayman Digital

Original note: [[SaymanDigital Story (English)]]

Part of [[Sayman E-Commerce Case Study]]. English version of [[SaymanDigital Story (Farsi)]].

> [!info] At a glance
> - **Client:** Sayman Digital, an e-commerce business launched on WordPress and later rebuilt on Laravel
> - **Engagements:** three separate returns over several years: 2015, 2017, and 2019-2020
> - **Core role (2019-2020):** Development Team Lead, leading a five-person team through a full WordPress → Laravel migration
> - **Scope:** requirements, architecture, platform evaluation, hiring, developer process, and hands-on execution
> - **Scale at handover:** 5,000+ products, 20,000+ daily visitors, ~100 orders a day
> - **A year later:** 274,000 clicks and 7.38M impressions from Google Search in a single month

---

### 2015 - First engagement: consulting on a stalled build

Sayman Digital brought me in as a consultant in 2015, while their store was still being built on WordPress and had not launched yet. Both the WordPress build itself and the way the team was working on it were causing problems.

#### The diagnosis

The picture was clear once I got into it. The WordPress developer on the project was slow and was not producing the output the business needed, and the team was not using git or any real development tooling.

My assessment was that Sayman would eventually need a fully custom-built system. My role became laying out that system's initial architecture and a software roadmap toward it, while making sure whatever shipped in the meantime was solid.

#### The recommendation

A full custom rebuild was not the right call yet. Sayman was an early-stage company, and that kind of build is expensive before the business can support it.

So I recommended a phased path: ship a proper WordPress store first, with the right person building it, then grow into a custom platform once the business had earned that investment.

#### The outcome

We brought in a more specialized WordPress developer to fix the execution, and a working version of the store launched soon after.

From there the team moved to a custom theme and custom plugins built for Sayman Digital. That turned a generic WordPress build into a proper specialty e-commerce platform, as the roadmap called for.

---

### 2017 - Second engagement: infrastructure, hiring, and pricing

The second time I joined, development of the WordPress store was moving along on its own track and a strong development and content team had formed. Following the path set a couple of years earlier, the system had shifted from an off-the-shelf theme to a custom theme and plugins built specifically for the business.

This time my work went beyond a single product. I helped with recruiting, and I set up core infrastructure the team did not yet have: a self-hosted GitLab instance and the server it ran on.

The project I led was about pricing, one of the most important operations in any e-commerce business. We wanted to be able to update prices quickly, and to see competitors' prices well enough to stay competitive. I built an initial version of that system.

My working relationship with Sayman wound down that year, and the idea never went past its first version. It came back later, and at much larger scale, in the rebuild.

---

### 2019-2020 - Third engagement: rebuilding the platform

#### Where the company stood

By 2019 the WordPress version had matured into a substantial custom build. As a regional store it had 20,000+ daily visitors and a catalogue of over 5,000 products, processing roughly a hundred orders a day.

This was where WordPress started showing its limits. The option that had once been the best for this company, and had produced its best results, was now holding it back.

Sayman Digital was now an established business with stable revenue. The first time I joined, the concern was getting started and launching quickly. Now the mindset had to change. Every operation, from supply and warehousing to sales and support, needed software that supported it instead of something people worked around. So one of the first things I set up when I came back was an internal ERP deployment.

#### Auditing a project already in flight

Before I rejoined, the company had started another project on its own: a companion to the store showing competitive prices across the market, with social features so users could discuss products and suppliers.

It was an appealing project and it had come some way. But after reviewing the code and the state of the work, I thought a result was still a long way off.

This was probably the first moment management saw the gap between their vision for launching a product and what the team could actually deliver. The root cause was familiar: no real documentation of the project's current state or its roadmap. That had distorted the team's own estimates and left engineering and management without a shared idea of what was being built or what was deliverable.

We set the project aside so the full team's capacity could go to the main rebuild. The decision mattered more for the rule it set than for the project itself. From then on, nothing went ahead without documentation and an agreed scope.

#### How I ran the requirements phase

This is where most rebuilds quietly fail. The people who know what a system has to do are rarely the people who can describe it in technical language, so requirements end up written by engineers guessing at the business, and the gap only surfaces after the build.

So the requirements document opened by telling the business the opposite of what they expected: **no technical language was needed.** Instead, there were three ways to contribute.

| Contribution type | What it captured | Example |
|---|---|---|
| **Musts** | Non-negotiable qualities of the new version | "Must support 500 concurrent visitors"; "must be fast and flexible when updating prices" |
| **Ideas and wishes** | Deliberately unformed ambitions, understood to need refinement before becoming technical work | Anything that would make the system stronger |
| **New technical capabilities** | Concrete, specific asks with detail attached | Multi-vendor support |

Splitting it three ways let people contribute at the level they actually knew. They did not have to overreach into design, and they did not have to stay silent because they could not write a spec.

What came back was the real business:

- Hundreds of near-identical customer comments every day, each answered by copying and pasting from a set of stock replies
- Pricing, described by the business itself as one of the company's biggest problems: the time it took, and the errors it produced
- Bundled products, which the existing system could not express
- Phone-system integration, so order follow-up could show why a customer had called and how far their case had progressed
- Identity tracking across a buyer's full journey, from first visit through review
- Measurability for sales, discounts, content, supply and packaging, and for the development team too

Every automation we later built traces back to a line in that document. We chose each piece of work because someone in the business had described the pain it removed, not because it was interesting to build.

#### Build or buy: evaluating the alternatives

In September 2019, before committing to a custom build, we ran a real evaluation.

We compared several open-source Laravel storefront platforms, **Bagisto, Aimeos, AvoRed, GetCandy, and Vanilo**, and mined Magento's much larger feature set for ideas about what a mature store needs.

Aimeos went furthest before we ruled it out, for concrete reasons:

- The core features we needed sat behind paid extensions, and those extensions depended on Elasticsearch and Apache Solr. Both are powerful, but they add a real infrastructure and knowledge cost on top of the licence
- Developer documentation was thin; in practice, understanding the system meant reading its source
- The paid extensions covered one year of updates, then required paying again
- Even after buying in, we would still need custom development to meet the requirements specific to our market. So "buy" did not remove the build. It added a subscription on top of it

#### Estimating the work

We broke the system into roughly **25 subsystems**: products, content, users, notifications, comments and ratings, order processing, discounts, marketplace, accounting sync, API, app management, performance monitoring, cart, files, system event logging, and more.

Then every feature inside them was estimated independently by four developers, including me.

The sheet kept two totals: the maximum estimate across the team, and **the maximum excluding mine**. That second column was deliberate. I was the lead and the most experienced person in the room, which meant my numbers carried more weight than they deserved and would anchor everyone else's. Keeping a total that excluded me was a cheap way to check whether the plan still held without my influence. For the record, my estimates were usually the highest in the sheet.

Averaged out, the work came to roughly **1,700 hours per developer**. That exercise, not the platform comparison alone, is what turned "let's build our own" from a preference into a costed decision the business could approve.

#### Building the team

We started with four people with quite different skill levels, so managing the work and dividing it by ability mattered from day one. We grew to five over the following sprints, across backend and frontend.

We were also deliberate about *when* to add people. Rather than hiring immediately, we waited a few weeks until the existing team had settled into the new development structure. That way we were not fighting onboarding and a new process at the same time.

#### What we built

The result was a Laravel and React platform with marketplace capability, migrated off WordPress with near-zero downtime. Products, users and full order history moved without the store going dark.

Beyond the storefront:

- **Operational tooling**: bulk price updates, advanced invoicing, and discount management scoped by user, product, and product variation
- **Omnichannel notifications** across email, SMS, web, and app push
- **Permissions and roles**, plus a documented RESTful API covering users, stores, products, pages, categories and site options
- **Accounting synchronisation**: orders posting automatically into the accounting system, with validation that blocked mismatched serial numbers at entry instead of surfacing them during reconciliation
- **KYC and fraud prevention**: scoring signals like account characteristics, prior order history, and payment-card verification. This module already existed in the old store, so rather than rewriting it we extracted its classes for reuse
- **A price-monitoring service** (Python, Django) that crawled competitor sites and surfaced relevant price changes automatically
- **Back-office automation** (Python, Flask, Selenium) for regulatory registration, external registry lookups, and bank identity verification. None of these had an API of their own, so we automated them by driving the web panels directly

That last item needs a word. When the external systems a business depends on offer no integration path, you can leave the work manual forever or automate the interface that does exist. We scripted the browser.

#### Going remote mid-project

We started in person, but COVID and the lockdowns arrived partway through.

Because the team already worked from written process and documentation inside the project-management system, we were ready for remote work when it came. The mechanics survived the transition intact. Communication was the harder part. Keeping a team connected remotely was a cultural shift for everyone.

Meanwhile the old platform still had to run. Our team included the developers who had built it, and because we had documented it first, we already knew which parts to maintain and which improvements to let go. COVID drove more online shopping, which meant more load on exactly the system we were replacing. We kept its user experience, speed and SEO in good shape, while putting as much capacity as possible into the new build.

#### Measuring delivery

Across four two-week sprints between November 2019 and January 2020, task completion moved **57% → 87% → 84% → 89%**.

The first number is as informative as the last. That sprint was disrupted by an infrastructure failure outside the team's control, and the retrospective named it plainly rather than absorbing it into a vague shortfall. Knowing exactly why a sprint missed makes the next one predictable.

By this point the team was also operating under a written scoring rubric covering timesheet discipline, peer sprint scores, task completion rate, and separate scores for the scrum master and for management. So by the end of 2019 this was a team with formal Scrum roles that held itself to measurable standards.

#### Closing the loop with the team

In December 2019 I ran a structured retrospective across the team, asking what single thing they would change, what they personally wanted to fix, how team management could improve, and what could be done about our processes.

The useful part was sorting every answer by **who could actually act on it**: management, the individual, or the team. That way nothing landed in the gap where everyone agrees a problem exists and no one owns it.

The team asked for time to mentor juniors, time to study and stay current, private per-sprint feedback, and more attention to testing and CI/CD.

When the development process was formally written up later, those items were its headline goals. We asked, and what they asked for became part of how the team worked.

#### Beyond engineering

I kept consulting for Sayman after I stepped back from day-to-day work, and by mid-2021 the brief had widened past the development team. I was asked to draft the company's working processes as it grew: salary structure and transparency, a continuous evaluation system, seniority and loyalty factors, defined career progression, quarterly team goals, and proper onboarding packages for new hires.

I will be straight about this one: that document was never finished. Its incentive and penalty sections are still empty headings. But being asked to write it at all says something about how far the role had travelled from "lead the developers."

#### Hiring the next developer

After the rebuild shipped, I designed and ran a technical hiring round for a Laravel developer: a test-project brief plus a written assessment I built myself. It covered three areas, not one:

- **Framework depth**: middleware, validation, polymorphic relations, query scopes, queues, resource collections, and testing
- **Version control and collaboration**: commit hygiene, branching, and what to actually look for when reviewing someone else's pull request
- **Process fluency**: breaking a real feature into estimated units of work, and how they would participate in a daily standup

Candidates were assessed on all three. Writing correct PHP was the minimum. The questions were designed to show whether someone could work inside a team that had standards.

---

### The culture we built

#### Shipping and delivering

As results became tangible, we increased how often we delivered. CI/CD had been in place from the start, but early on the team's output only reached management at the end of each sprint.

That became a clear, measurable weekly report, backed by a usable version of the system permanently available for testing on staging.

Building a large product for an established company means the biggest risk is not technical. Beyond the obvious stakeholders there were regular customers, support staff, warehouse operators and supply staff. The real danger was everyone holding a different idea of what was being built.

Using agile principles, we worked to keep a shared understanding alive in every design decision, not just every sprint. That never meant accommodating every opinion. It meant being explicit about which decisions we were making, which we were deferring, and which we were sacrificing outright. Then we followed through on necessary refactors without flinching, as long as a usable version always existed.

Delivery meetings grew more frequent, sometimes twice a week, and the audience widened past management to the support and warehouse teams, who by then were testing the system themselves.

That did double duty. It kept everyone aligned, and it built familiarity with the new system well ahead of the migration.

> One of the biggest risks in any migration is how comfortable an organisation's people feel about the change. Everyone always believes the old system was better. Starting familiarity early tells people their input is being weighed, and turns them into partners in the build rather than people the build happens to.

In effect the development team was building the product in front of the whole company. Delivery meetings raised the pressure at first, but shipping and presenting every time built confidence, and that meant more deliverables at every step. Features reached test servers fast enough that the feedback loop (bugs, requests, UX changes, notes for later) stayed short.

#### Communication

Communication was one of the first things I found broken. The side project that had started without me had very little of it, which is also why its documentation was thin.

The old system's track record had earned real trust between management and the original developers. Anyone newly added started outside that trust by default. That gap showed up as unclear, inefficient communication between the established developers, the newer ones, and management.

My own emphasis on documentation did not automatically fix it. If anything it sometimes crowded out the value of simply talking to each other. Documentation that nobody reads is not communication.

The fix was ordinary, and it worked: more meetings, reading documents aloud together rather than assuming they had been read, and making sure everyone knew their feedback was heard and acted on.

We put deliberate weight on the phrase **shared understanding**. That did not mean unanimous agreement on every approach. It meant always being able to explain the direction and name the blockers, even when not everything could be solved. Sprint meetings, daily standups, and open reports built that over time, both day to day and for the bigger picture.

#### Ownership

Getting work from planned to delivered required a real culture of ownership. In a company this size, a planned task usually needs more detail before someone can act on it, and the person doing the work has to chase that detail rather than wait for it.

We wrote this into the developer handbook as one governing line:

> **The owner of a task is the owner of that task's details.**

In practice:

- Every task lived on the board with a clear name, an owner, tags, a description, and any attached files or discussion, moving through **Todo → Doing → Today → Review → Done**
- **Today** held only tasks detailed enough to start immediately and small enough to finish by end of day. The test for whether something was broken down far enough was blunt: *can this be done in a block of one and a half to two hours?*
- Whoever took a task followed it from chasing the missing detail, through the code, to the merge, including talking to anyone the task depended on
- Every task got its own branch, named `[description]-TYPE#TASKID`, where `TYPE` was one of `feature`, `enhance`, `cleanup`, `refactor`, `fix`, or `hotfix`. Branches that ignored the convention did not get merged
- Pull requests stayed small enough to really review, and stated what they did and which task they advanced or closed
- Time was logged against the task as a formal step of the workflow, not an afterthought

Owning a task end to end, from the details needed to start through the code and the documentation, creates a much stronger sense of responsibility than handing work off does. It also means every dependency gets surfaced by the person doing the work, rather than discovered later by someone else.

---

### Scale, a year after handover

In **June 2021**, roughly a year after the rebuild shipped and after my day-to-day involvement had ended, the platform recorded **274,000 clicks** and **7.38 million impressions** from Google Search in that single month.

Most of the credit for search numbers belongs to the marketing and content teams, and by then the platform had been running and evolving without me day to day for a year. So I don't count this as my result.

What I can take from it is smaller. A year after I stepped back, the team was running the platform on its own, and the system we built was still carrying that much real commercial traffic.

---

### What I take from it

Three separate returns to the same company, years apart, says something on its own. Each time it was a different problem: execution and tooling in 2015, a specific operational system in 2017, and a full platform and organisational rebuild in 2019.

What ties them together is that each engagement left something behind that outlived it. A WordPress store that grew into a full specialty platform. Infrastructure a growing team could stand on. And finally a Laravel platform, an internal ERP, and a development culture that kept running and growing long after my day-to-day involvement ended.


---

## Asr'e Ahan

Original note: [[Asr'e Ahan Story (English)]]

Part of [[Asr'e Ahan]].

![[Attachments/AsreAhan/Logo/asreahan-logo.png|420]]

> [!info] At a glance
> - **Role:** IT consultant / advisor. Not a full-time hire, and not the implementation team
> - **Started:** 8 July 2020, in the middle of the COVID pandemic
> - **Commitment:** 20 hours per month on retainer, with a written report at the end of every month
> - **From first meeting to a developer under contract:** about nine weeks
> - **Result:** a hired team, a documented development process, a shipped version one, still running and still being updated more than five years later

---

### Who the client was

Asr'e Ahan is a steel and iron trading business with more than 35 years behind it. The company started trading iron and steel in 1989, built its position the traditional way for that industry, on relationships, phone calls, and physical markets, and by 2019 had decided it needed to be online. It added an e-commerce arm and launched a marketplace for steel sections, connecting producers, distributors, and buyers directly: live pricing across the different steel products, market news, shipping, warehousing, credit sales, and pre-orders.

That combination is what makes this engagement interesting. The company was strong and experienced in its own field, and it was entering one where none of that experience transferred. They knew steel. They did not know how software gets built, how developers are evaluated, or what a healthy development process looks like. Most important, they had no one inside who could tell good technical advice from bad.

### The call before the call

My friend Mohammad called me: a startup he knew was looking to hire a developer. He asked my opinion about the candidate they wanted to bring on, and I ended up putting together their contract for them: both the technical points they needed to cover and the clauses that belong in a software agreement.

That day I told them something they did not act on. They would be better off having an IT consultant alongside them to guide them. A development team on its own can lose its way, or lack a long-term view on the deeper things, such as maintainability and the system's capacity to grow.

### The second call

A few months later I got another call from the Asr'e Ahan team.

They had gone ahead without a consultant alongside them, exactly the way I had warned against. Months had passed. Money and time had been spent. There was no real output, the stakeholders were frustrated, and, worst of all, nobody could say clearly what had been built, what worked, or what was left to build.

That is the point where I came in.

### What I was actually hired to do

We signed a consulting agreement with a deliberately broad scope:

- Reviewing and proposing IT solutions that actually moved the company's goals forward
- Establishing and improving the software development process
- Building and maintaining the development roadmap **together with the stakeholders**
- Evaluating and reporting on how the work was being executed
- Recruiting and hiring the technical team

It was a retainer, not a full-time role: **20 hours a month**, with a written report to the client at the end of every month. Everything described below was built inside that budget.

> That constraint is the point, not a footnote. A company at this stage does not need a full-time executive it cannot yet justify. It needs the right decisions made in the right order, and someone accountable for them.

### Working through a pandemic

One more thing shaped all of it: this was the middle of COVID.

We wrote it directly into the contract: the work would be done through online meetings and remote collaboration, and if conditions worsened we would renegotiate *how* to continue, not *whether* to. The developer employment contract we later signed said the same thing: remote by default, no fixed place of work, occasional office visits by arrangement.

At the time, remote work was not yet the default it later became. Most teams here were treating remote as a temporary emergency and waiting to go back to the office. We decided to treat it as the permanent shape of the team, and to design everything else around that assumption.

### Point A: knowing what already existed

The first thing we did was document the existing system. We mapped the development work that had already been done and the current state of the system, and treated that as point A.

That included doing it myself. I went through their self-hosted GitLab, installed the previous team's source code, and ran and tested it myself. You cannot assess a codebase from a meeting. Four hours of actually standing the thing up told us more about what could be salvaged than any amount of discussion would have.

This step also answered the question the company could not: **what do we already own, and what is it worth?**

### Ending with the old team without losing the work

The previous developer, after frequent conflicts with the stakeholders, was no longer really collaborating, and was blocking the changes the development process needed. We decided to part ways.

But it mattered to us that the earlier effort would not go to waste, and that we would not restart from zero. So instead of simply terminating, I wrote a short handover protocol. It took 45 minutes and it committed both sides:

- The departing developer hands over the **latest** version of all code, the database, all design and engineering documentation, and every other artifact produced for the project
- He **explains how to use them** (source code, database, documentation) rather than just dropping a repository and leaving
- He cooperates with and advises the incoming developer or team
- The company pays everything owed through the final day
- The company **also pays for the hours spent on the handover itself**
- A portion of the payment is held back as a good-performance guarantee, released once those obligations are met

That last pair of clauses is the whole design. A clean handover was made the rational, paid choice for the person leaving, rather than something we had to hope for out of goodwill. Most companies in this position lose everything they paid for in the previous chapter. Asr'e Ahan did not.

### Hiring: process first, then people

The order here surprises people, so I want to be precise about it. Before we wrote the job ad, and before we ended things with the old team, we wrote down how development would work.

| When | What |
|---|---|
| 8 July 2020 | First meeting: initial discussion and planning |
| 10 July 2020 | **Drafting the development process documentation** (the longest single item that month) |
| 11 July 2020 | Getting access to the company's GitLab; meeting with management |
| 22 July 2020 | Writing the developer job ad |
| 24 July 2020 | Writing the old-team handover protocol |
| 4 August 2020 | Reviewing GitLab, installing and testing the existing source code |
| 5-8 August 2020 | Screening resumes, coordination |
| 13 September 2020 | New developer signed |

We wrote a clear job description and listed what was really needed to carry the work forward and finish it. We wanted a team that would build both frontend and backend on JS, so we looked mainly for **full-stack developers**. That came from the flexibility we needed:

- It was not yet clear how much of the existing system we could reuse
- It was not yet clear which parts of the road ahead should be built first
- We wanted to be able to move people between areas as those answers emerged
- And full-stack people would read the existing code more easily and understand all its parts

#### Hiring under COVID

The pandemic made this much harder.

The candidate pool itself had changed. People were reassessing their jobs, some were leaving the market, and others were suddenly open to working for companies in other cities because everything was remote anyway. Meanwhile we had to judge people we would never meet in a room: no shared whiteboard, no walking them past the team, none of the informal signals you normally rely on.

And we were hiring for a company whose stakeholders had just been burned by a developer who stopped collaborating. So communication and collaboration under remote conditions were not soft criteria for us. They were the thing we were most afraid of getting wrong.

We built a system for evaluating candidates, filtered the resumes down to a shortlist, and ran the entire process online.

### The developer handbook

In parallel with hiring, we wrote the document that turned out to matter more than anything else I produced there.

To make sure the new development team (and everyone hired afterwards) shared the same understanding of our standards and process, we created a **developer handbook**. It described how work actually moves, end to end:

- Every piece of work starts as a task on a single GitLab board
- Each task carries everything needed to do it: a clear name, an owner, an estimate, labels, a description, and any attached files or discussion
- Work moves through defined columns: **Open** (the backlog), **Doing**, **Today**, **Review**, **Closed**
- **Today** holds only tasks small enough to be finished by the end of the working day, and specified in enough detail to start immediately
- Every task gets its own branch, following one naming convention, tagged by type: feature, enhance, cleanup, refactor, fix, hotfix
- Every branch ends in a pull request, small enough that another person can really review it, linked back to the task that motivated it
- Estimated time and actual time are both recorded against the task

We did not invent anything new. The company's git was already self-hosted on GitLab, so we ran project management on that same GitLab instance rather than introducing another tool.

#### Why we kept it small

We deliberately kept the handbook short and simple. We did not want it to become a burden, and we did not want it to become the kind of document nobody reads. The test was that someone joining the team should be ready to work after a short read.

That constraint did more than it seems. A long process document gets ignored the first time there is deadline pressure, and once it has been ignored, it is dead. A short one survives, because following it is cheaper than working around it.

#### Designed for a team that was never in the same room

Both the handbook and the development flow had to work for a team that was fully remote, and that assumption changed the design.

Nothing could depend on someone turning around and asking the person next to them, because there was no person next to them. Decisions had to leave a written trace. The state of any piece of work had to be readable from the board rather than reconstructed from a conversation. A new hire had to be able to onboard themselves.

Today that sounds obvious. In 2020 it was not.

#### We made it binding, and we made it part of hiring

Two decisions gave the handbook real weight.

First, we wired it into the employment contract. The new developer was contractually obliged to work according to the company's documented internal standards, which had to be provided to him in written form, with changes effective from the moment they were communicated. The handbook was not onboarding decoration; it was part of the agreement.

Second, we used it in interviews. Every candidate who moved past the first stage read the handbook, and in the next stage we asked them either to explain it back to us or to tell us how they would improve it. That did three things at once: it tested how they think about process, it told us whether they could absorb written material without hand-holding (the core remote skill), and it meant nobody ever joined surprised by how we worked.

#### Why this one document outlived me

Of everything I built there, the handbook is the piece that kept working after I left, and I think the reasons apply elsewhere, so here they are.

**It made the process self-describing.** The board was not a reporting layer on top of the real work. It *was* the work. Any question about what was happening, what it cost, or who was waiting on whom could be answered by looking, not by asking. When the person who designed a process has to be present for the process to run, that is not a process; it is a dependency. The handbook removed me as a dependency on purpose.

**Its simplicity is what kept it alive.** Because it was small, it could be read in one sitting, argued with, and changed. Teams inherit documents they are afraid to touch, and those documents rot quietly while everyone works around them. This one was short enough that improving it was a normal, low-stakes act; we had invited candidates to critique it before they were even hired. So it kept changing instead of hardening. The version running there now is not the version I wrote, and that is what I intended.

**Its transparency made the process outcome-based rather than activity-based.** Every task had an owner, an estimate, a real time spent against that estimate, a reviewer, and a definition of done that ended in merged code. That combination makes it hard to be busy without producing anything, which is exactly the failure the company had just lived through. Nobody has to trust a status update when the status is visible.

**It gave the rest of the company a door in.** Other teams and stakeholders (marketing, SEO, the production units) filed their own requirements onto that same board, in the same format. That single decision did more for the relationship between the business and the development team than any meeting could have. The technical people stopped being a black box, and the business people stopped having to ask a favor to get something looked at. They could see their request, see its priority, and see it move.

That is why the handbook mattered more than the code we shipped. Code gets replaced. A simple, transparent way of deciding what to build next does not. It keeps paying off.

### Shipping version one

With the process in place and the team hired, we made the foundational decisions together: the tech stack, which of the existing code should stay and which should go, and what needed to be built new.

Because so much time had already been lost with no clear output, everything pointed at one goal: **publish version one**. Every decision served that goal. That included knowingly leaving places we would have to change later, because it was not the right moment to refactor.

In a short time, we shipped the first version of the Asr'e Ahan platform.

Right after that we built a roadmap from the ideal big picture and worked out what maintaining and updating the system would take with very short release cycles. I used my engineering background to find the real structural weaknesses, and we scheduled the refactors we had deliberately deferred.

### Working with stakeholders over video

Everything needed to increase the team's velocity came out of weekly work with the development team, the management team, marketing and SEO, the production units, other iron production factories (to understand the industry properly), and the rest of the stakeholders. That meant documenting requirements, and the non-software processes needed to discover new parts of the system and how they should behave.

Nearly all of it happened online, and this was the part that took the most patience.

Running a remote development team is one thing. Running weekly requirements sessions over video with people who had spent thirty years doing this business face to face, on the phone, and in the market is another. Some of them had never worked that way in their lives. So part of the job was simply making the format work:

- Keep sessions short and specific rather than long and general
- Write down what was agreed and send it back, so nothing depended on memory
- Go to people individually when a group call was not producing the detail we needed

The documentation habit that later spread through the company started here, out of necessity. When you cannot walk down the hall to check something, writing it down stops being bureaucracy and becomes the only way the work moves.

### Roadmap and reporting

The roadmap was never something I handed over finished. It was built and updated together with the stakeholders, which is the only way it stays honest: they own the priorities, I own translating those priorities into something a development team can actually build against.

Alongside it, at the end of every month the client received a written report: what had been done, what was blocked, what was coming next. After a period where months had passed with no visible output, that cadence mattered nearly as much as the work itself. Nobody had to wonder where things stood.

### The results

- The development team had a clear roadmap and simple, unambiguous guidelines to build against
- Management and the main stakeholders had someone who could translate their needs into the development team's language, and could be confident the output would still be usable years later
- Documenting the current state, the target state, and the requirements to get between them was a simple move that spread to other teams
- Those teams not only documented their own processes better, they knew their technical needs would be answered through a defined process rather than through personal relationships

### Five years later

![[Attachments/AsreAhan/Logo/social-logo.jpeg|120]]

Asr'e Ahan has continued for **more than five years** with the development team I hired and helped start, and it still does. The system we built is still running and still being updated.

It is also in real use. The platform now handles around **60,000 visits a month** and carries **63 supplier partners** trading on it. Those are today's numbers, years after my involvement ended, and they belong to the team that kept building. My part is narrower. I hired the team, helped write the process, and helped ship version one. What I count is that version one is still running and still being updated more than five years later.

That is the actual goal, and it is a higher bar than shipping: a good software product built alongside a good software development process, both of which outlast the consultant.

### What I take from it

Asr'e Ahan is a good example of a company that can benefit from a consultant who spent many years as a practitioner and is not afraid of execution.

It is also the example I reach for whenever I need to explain the difference between doing this with a good consultant and doing it without one, because this company did both, in that order, and the contrast is unusually clean.

That difference matters most when you are established and strong in your own industry but only now entering the business of building software. Your existing expertise can fool you about your competence in this one. A good consultant prepares you for the risks and the opportunities ahead, builds better communication between the different partners in the software production chain, and makes sure the path you have laid out is actually being followed.
