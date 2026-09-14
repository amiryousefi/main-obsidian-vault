---
created: 2026-09-14
---
# My Story (English)

Part of [[Todays Crypto Case Study]]. English version of [[Today's Crypto Story (Farsi)]].

> [!info] At a glance
> - **Client:** Today's Crypto (TC), a Swedish startup building a video platform for the crypto community, backed by the founder's company, EQ Gruppen
> - **Role:** CTO, from December 2020 to early 2025. I came in to rebuild a failing codebase and stayed to own architecture, team, delivery and production
> - **Team:** four core engineers (me, frontend, backend, panels), later joined by a smart-contract engineer and a UI developer. On the client side: the founder/CEO, a QA and product owner, and a partnerships lead
> - **What we built:** a three-part platform (Next.js viewer app, React publisher and admin panel, Laravel API), a Python YouTube importer, a Node.js blockchain integration service, and the TCG token contracts on Polygon
> - **Web3 layer:** wallet login, the TCG ERC-20 governance token (5 billion fixed supply), watch-to-earn rewards with on-chain claims, vesting wallets, NFT-based HODL memberships, and crypto payments
> - **Milestones:** closed beta on 9 May 2021 · public publisher launch August–September 2022 · desktop launch December 2022 · TCG live on Polygon mid-2023 · first community airdrop in November 2023, with **2,000+ signups on day one** and **~10,800 unique visitors a day**
>
> For the short, site-ready version see [[TodaysCrypto — Website Case Study]]. For the full feature inventory see [[Platform Feature Report]].

---

## Who the client was

Today's Crypto was the idea of a Swedish entrepreneur who already ran an established consumer-products company, EQ Gruppen. The pitch was simple: a YouTube for crypto. Crypto creators were posting on general-purpose platforms that did not care about their niche. Their audience lived in wallets, tokens and price charts. They should have a home built for them.

Simple to say, hard to build. A video platform on its own is already a big product: upload, transcode, watch, subscribe, comment, recommend, monetise. This one also had to feel native to crypto users, which meant wallet login, live market data, a token economy and on-chain ownership.

The founder had business experience and a strong product sense. What he did not have was a working codebase or a technical team.

## How I came in

In November 2020 I was introduced to the founder through Proxify, a Stockholm-based network that matches vetted developers with companies. The first call was on 12 November 2020.

The project was not starting from zero. It was starting from below zero. A previous developer had built a first version, and his own handover notes, sent to the client and me the same day, were blunt about it: *"the whole script is bad and I think this script is not intended for modification by other developers."* No autoloading, no package manager, no MVC, routing through `.htaccess`, PHP and JavaScript mixed in the same files.

The founder's reaction was the right one: *"If there is that much code that needs to be replaced, we need to look into this and see if it's worth the time."*

It was not. I recommended a rebuild, and we started one. By **30 December 2020** the first deployed version of the new platform was running, with home, category, video and channel pages, subscribe, likes and bookmarks. Signup and login followed two weeks later.

From that point I was no longer the developer on the project. I was the person responsible for the technology side of the company, and formally its CTO.

## Rebuild, not repair: the architecture

The early decisions are the ones that carried the product for years, so they are worth being precise about.

**Three surfaces, one API.** A Next.js web app for viewers, a single React application for both publishers and admins, and a Laravel API behind both. Viewer work, creator tooling and back-office features could each ship on their own schedule without blocking each other.

**Server-side rendering for discovery.** A media platform that search engines cannot read has no organic reach. Next.js with SSR was chosen for SEO, not fashion.

**Mobile first, literally.** The crypto audience is on phones. For most of 2021 the product *was* the mobile web app (internally "MWA"), with separate mobile and desktop component trees per page. The desktop web app came later, launched in December 2022.

**Split data by access pattern.** Business records in MySQL. Watch time, token points and channel statistics in MongoDB. Write-heavy behavioural data does not belong in the same store as users and payments, and that separation later made the token system possible.

**Media off the application servers.** Video moved to object storage, first S3 and then Cloudflare R2, uploaded directly from the browser with pre-signed URLs, so large uploads never passed through the API.

**Three environments from the start.** `beta` for daily integration, `cl-beta` for the closed-beta users and the founder's testing, and production. That discipline is what later let a small team deploy several times a week without breaking what testers were using.

## Building the team

I started alone. In January 2021 I brought in the first engineer, a frontend developer I trusted, at the same rate as mine. By mid-2021 a backend engineer and a second frontend engineer, who would own the publisher and admin panels, had joined. That team of four built the core of the platform and stayed together for most of the next four years.

The team later expanded for specific needs: a smart-contract engineer for the token work in 2023, and a UI developer in 2024. When we needed a small, self-contained tool in 2021, I brought in a contractor from my network on a fixed budget rather than growing headcount. The founder added a bonus if it shipped, integration included, before a set deadline.

On the client side the team grew too: a product and QA owner who tested every ticket before release, and a partnerships lead who signed creator channels.

## The working rhythm

We were a distributed team working with a founder in another country and another time zone. The mechanics that made that work were deliberately simple.

- **Regular syncs** with the founder at a fixed time, 10:00 CET (our late morning), plus Loom walkthroughs and voice notes when a meeting did not fit.
- **The founder as the first real user.** Every build went to him on his own phone. When an iOS-only bug showed up that we could not reproduce, we added BrowserStack so we could test on the same devices our users had.
- **A shared board.** Trello from July 2021, then Jira with separate projects for the 1.0 platform, the ongoing improvement track, and the TCG token integration. Tickets moved through *Backlog → Selected for Development → Business QA → Ready for deployment → Done*, so nothing reached production without passing the client's own QA.
- **Sprint planning with the client.** The founder and the product owner set priorities. I turned them into child issues, estimated them with the team, and briefed each developer.
- **Radical time transparency.** From May 2022 every developer kept a daily log, with hours and what was done, in a report the client could open at any time. Invoices matched those logs.

That last point matters more than it looks. A startup that is bleeding money needs to see where it is going. Nobody on the client side ever had to wonder what the team did last week.

## Closed beta: May 2021

Five months after the rebuild started, on the night of **9 May 2021**, I wrote to the founder at two in the morning: *"WE ARE UP."* The closed beta went live with imported videos from the first two channels, sorted into BTC, ETH, altcoins and DeFi categories.

What followed was the normal, unglamorous part: fixing a related-video playback bug, a drawer that rendered wrong on some iPhones, avatar uploads from the camera, font sizes. Then we restructured the video page, the core page of the product, for speed, and rolled that pattern out to the rest of the app.

Over the rest of 2021 the product started to look like itself:

- A live **coin ticker** under each video and a **market drawer** on every page, ranked by market cap. The founder's comment when he saw it: *"Now I don't need CoinMarketCap anymore."*
- **Coin pages** with detailed market data from the CoinMarketCap API
- **Video chapters** and a custom player with tap-to-unmute and a minimised mode
- **Real-time notifications** across all three surfaces
- **Stripe** subscriptions

## From beta to a real platform: 2022

2022 was the year the platform had to become something the company could put in front of real creators and real users, and then in front of investors.

The work that year was mostly trust infrastructure:

- **Two-factor authentication** by email code and by authenticator app (TOTP with QR code), with a hard 2FA gate on sensitive actions
- **KYC with iDenfy** for publishers, so creators could be paid in a correct and legal way, with every change to payment details logged
- **Six-digit email verification** instead of activation links
- A full **comment manager** for publishers: read/unread, mentions, pinning, follow-up flags
- **Chromecast and AirPlay** casting in the video player
- Landing pages for users and publishers, launched publicly in August 2022

In September 2022 the founder sent the team a letter. The company had been *"bleeding since we started this project,"* it now had software *"so good that we feel confident inviting real users and content creators to it,"* and it needed real user data to raise more money. The development budget was cut, temporarily.

That changed what "most important" meant. The biggest barrier to growth was content, and no established creator was going to re-upload their whole library to a new platform. So we built a **YouTube importer**. A publisher connects their channel, and the importer pulls the back catalogue and keeps syncing new uploads, with titles, descriptions, thumbnails and chapters.

The first real creator channel was imported overnight in September 2022, about a hundred videos by morning. Brand channels followed, including CoinGecko and OKX, and over the next year more than a dozen crypto channels were onboarded. The desktop web app launched in December 2022.

## The Web3 layer and the TCG token

This is the part of the platform that made it Today's *Crypto* and not just another video site. It is also the part with the least room for error. On-chain mistakes cannot be rolled back.

### What users saw

- **Wallet login and registration.** MetaMask and WalletConnect through Web3Modal and wagmi, next to email/password and passwordless magic links. The backend verifies wallet ownership with a signed message (Keccak-256 signature recovery), so a user can create an account with nothing but a wallet.
- **Watch-to-earn.** Users earn TCG for engaging with the platform: 1 TCG per minute watched, 25 TCG for setting up a custom feed, 5 TCG per invited friend. They earn from the moment they sign up, with no wallet needed until they want to claim. There was no token sale. Tokens were meant for the people using the platform.
- **Claiming on-chain.** Earned tokens start as locked. Once they unlock, a user with at least 500 TCG connects their wallet and claims them to Polygon from the TCG page, which shows claimable, locked and total balances plus claim history.
- **HODL memberships as NFTs.** Two NFT editions minted on Polygon. The White edition (50 MATIC, capped at 100k) earns 1–3 TCG per minute watched, up to 180 a day. The Black edition (250 MATIC, capped at 20k) earns 5–15 per minute, up to 900 a day, and removes ads. The platform listens for NFT transfers and updates a user's membership status automatically when the NFT moves wallets.
- **Crypto payments.** Coinbase Commerce checkout next to Stripe. The simplified 2023 plans were $5 a month or $50 a year, with 5,000 TCG included in the yearly plan.
- **Governance and transparency.** A governance page describing TCG holders voting on content quality and new features, with voting power snapshotted before each proposal and 10% of platform revenue going to a reward pool for voters. A transparency tab listed every contract address and wallet so anyone could verify them on Polygonscan.
- **Crypto-native monetisation.** Publishers register a payout wallet, verified behind KYC and 2FA. Crypto brands run buy-button campaigns tied to specific coins. A "Cha-Ching" share card lets users post their earnings to social media.

![[Attachments/TodaysCrypto/ScreenShots/Web App/Token Earnings.png|700]]

### The smart contracts

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

### Design choices worth explaining

**Non-upgradeable on purpose.** The token was redeployed to testnet as a version *without* upgradeability before going to mainnet. An upgradeable token lets the team change the rules later. For a token whose value depends on holders trusting a fixed supply, that flexibility is a liability. Fixed code, fixed supply.

**A claimable ledger instead of a Merkle tree.** We first designed claims around a Merkle tree, which is the gas-cheap standard for airdrops. We shipped a simpler model: the backend writes per-user claimable amounts to the contract once a day, and users pull. It costs more gas on our side, paid in MATIC from the script wallet. In exchange every user's balance is readable on-chain, there are no proofs to generate or serve, and above all it creates a **daily control point** between "earned on the platform" and "claimable on-chain." As the next section shows, that control point turned out to be the most important security feature we had.

**Off-chain earning, on-chain settlement.** Watch time, referrals and engagement are tracked off-chain in MongoDB, where writes are free and fast. A Node.js integration service reads settled earnings from the platform API and pushes them to the reward contract at 00:00 GMT each day. Users get a Web2-speed experience, and only actual ownership transfers touch the chain.

![[Attachments/TodaysCrypto/ScreenShots/Web App/Token Governance.png|700]]

## When traffic finally came: the airdrop and the bot farms

On **1 November 2023** the company ran its first community airdrop campaign, ahead of an exchange listing. It worked better than anyone expected. **More than 2,000 users signed up on the first day** and watched more than a thousand videos. The Telegram group turned into what I called a notification bomb. I had to pull over while driving and mute it.

Within hours the platform started going down under the load. Within days we learned that a large share of that traffic was not people.

A token that pays for watch time and referrals is an open invitation to farms. What we saw:

- One referrer with **almost 10,000 referrals** and nearly 100,000 tokens
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

At the same time we were keeping the site up. We resized servers, profiled slow MySQL queries, and temporarily switched off server-side rendering so pages could be served faster under load. One day's analytics showed **10,770 unique visitors**.

Not everything went cleanly, and I would rather say so. One night the distribution wallet ran out of MATIC for gas, so claims stalled. A failed on-chain transaction made users' earned tokens look like they had vanished, and the Telegram group melted down until we traced it. A reward-limit change went live before the previous day's earnings had been made claimable, and it wiped them. We restored them the next morning. Each time, the fix was fast. The lesson was that a token community watches every number in real time, and every operational slip becomes a public trust problem.

## Keeping a startup platform up

For most of its life the platform ran on a very small infrastructure budget, and a lot of my work was keeping it standing.

- **January 2023:** after a server migration, MySQL query logging had been left on and filled the disk. We were down for an hour and a half. The founder asked for an incident log so we would not repeat mistakes. I added a scheduled cleanup, a shared incident log and a **server migration checklist**.
- **February 2023:** outages traced to CPU exhaustion from updating crypto prices every five seconds (slowed to twenty) and to the importer and beta API sharing the production server. We moved the importer and beta onto a separate server so the production API ran alone.
- **Early 2023:** repeated instability at our hosting provider, at the worst possible times, including the evenings when the company had just contacted dozens of US venture capitalists. In **May 2023** I migrated the whole platform to DigitalOcean.
- **November 2023:** a market-data service wrote 59 GB of logs in a few days of airdrop traffic and filled the disk. We disabled it and fixed its logging.

Uptime monitoring ran through Pingdom and edge protection through Cloudflare. Most incidents were fixed within the hour, often late at night. The honest weakness is that too many of those fixes depended on one person being reachable. I come back to that below.

## The importer: building on someone else's black box

The YouTube importer was the growth engine, and it was also the platform's most fragile dependency.

YouTube does not want its videos downloaded at scale. Over two years the importer broke because API quotas ran out as we added channels, because the open-source download library stopped working after YouTube changed its data format, because YouTube changed a few meta tags in its HTML, and because storage credentials were revoked. Each time it was fixable: more API keys, automatic restarts when quotas ran out, and eventually a rebuilt importer with more of the pipeline in Python that used far fewer API calls. In September 2023 it ran reliably for weeks, checking every channel every two hours.

But as I told the founder at the time, depending on YouTube was *"like trying to control a black box system."* By late 2024 YouTube was actively blocking this kind of downloading, including from new servers and through proxies, and the importer spent long stretches down. A content platform with stale content is hard to grow, and harder to raise money for.

## What didn't go well

The references I trust most include this section, so here is mine.

**Operations depended too much on me.** Deployments, server access and importer fixes ran through me for too long. When I was sick, which happened more than once in 2023 and 2024, the platform had no real on-call cover, and the founder was left chasing me for updates. It was a classic startup pattern: the person who built the system is also its only operator. I should have pushed harder, earlier, for shared runbooks, a second person with production access, and automated alerts instead of the founder noticing that no new videos had arrived.

**Alerting came too late.** The founder asked for importer alerts in February 2023. We built auto-restart in August 2023. That gap cost us weekends of stale content.

**A strategic dependency we could not control.** The importer made onboarding creators easy, and it tied the product's freshness to a platform that did not want us. A plan B, such as creator-side uploads, official partnerships or embedding, should have been treated as a priority, not a someday.

**Budget and morale.** After the 2022 budget cut, the team kept building, and in 2023 delivered the token integration, the migration and the airdrop response. By mid-2024 I told the founder plainly that motivation in the team was very low. By early 2025, with fundraising not closing, the engagement wound down.

## Where it ended

Today's Crypto ran in production from 2021 into 2025: a closed beta, a public platform for creators and viewers, a full Web3 token economy on Polygon, and a community that at its peak brought thousands of signups a day. It was built and operated by a core team of four engineers and a small client team.

The company did not reach the funding round it was working toward, and the platform is no longer live as Today's Crypto. The core infrastructure we built was preserved and carried into the founder's next venture, which is the most direct evidence I have that the architecture outlived its first product.

## What I take from it

Today's Crypto is the engagement where I learned what it means to be a CTO inside a startup rather than a lead inside a company.

The technical lessons are clear. Rebuild early when the foundation is wrong. Split surfaces and data stores by how they are used. Design token systems so there is always a point between earning and settlement where humans can still intervene. That last one is what saved us when real traction arrived together with the people trying to farm it.

The organisational lessons were harder. In a startup the CTO owns the product *and* the pager, and a system is only as reliable as the least-covered hour of the person running it. Transparency, like daily time logs, a client-run QA stage and an honest incident log, kept a long cross-border relationship healthy through budget cuts, outages and a very public token launch.

If I did it again I would build the same platform. I would build the operating model around it, with shared on-call, automated alerting and a second pair of hands on production, much earlier.
