╭─── Claude Code v2.1.133 ─────────────────────────────────────────────────────╮
│                                                    │ Tips for getting        │
│                 Welcome back Kiran!                │ started                 │
│                                                    │ Ask Claude to create a… │
│                       ▐▛███▜▌                      │ ─────────────────────── │
│                      ▝▜█████▛▘                     │ What's new              │
│                        ▘▘ ▝▝                       │ Internal fixes          │
│ Sonnet 4.6 · Claude Pro · kkpannu2013@gmail.com's  │ [VSCode] Fixed extensi… │
│ Organization                                       │ Added `CLAUDE_CODE_ENA… │
│      ~/Documents/Ai edge demo/Week1 Homework       │ /release-notes for more │
╰──────────────────────────────────────────────────────────────────────────────╯

❯ Help me write a complete, detailed PRD for my product Haute food fusion.      
  Before you begin, you must ask me any clarifying questions needed to ensure   
  the PRD is accurate and aligned with the expected user experience. Ask one    
  question at a time, to clarify all assumptions.                               
                                                                                
  Below is my product idea:                                                     
  --Context: To use it to invent original fusion dishes from world-wide         
  cuisine                                                                       
  --Components: The components in the app are that I want users to input their  
  2-3 cuisines, ingredients they have and skill level and then the AI can       
  generate a unique dish name, ingredients list, step-by-step recipe, plating   
  suggestion (high-end-feel)                                                    
  --Success criteria: The criteria I will set are: Users should be able to save 
   recipes.                                                                     
      •    Recipes should be cookable by real humans                            
      •    Recipes should have realistic timing                                 
      •    Recipes should use compatible ingredients                            
  Users should love the recipes and return weekly for new creations.            
                                                                                
  What I want from you: Before writing the PRD -> Ask me clarifications         
  questions across any topics you feel unclear. If you think there can be       
  feature, bring them up and discuss with me.                                   
                                                                                
  You must ask clarifying questions if anything is missing, unclear, or         
  contradictory.                                                                
                                                                                
  The PRD must include:                                                         
                                                                                
  - Problem Statement                                                           
  - Business success metrics                                                    
  - Personas & key user journeys for each persona                               
  - Technical success metrics                                                   
  - Scope of MVP                                                                
  - Technical considerations                                                    
  - UI style preferences (if product has UIUX)                                  
  - Corner cases                                                                
                                                                                
  ⎿  UserPromptSubmit says: Hookify import error: No module named 'hookify'

⏺ Great concept — let me make sure I capture it accurately before writing
  anything.

  First question: What platform(s) is Haute Food Fusion targeting?

  - Mobile only (iOS and/or Android)
  - Web app only (browser-based)
  - Both mobile and web from day one
  - Web MVP first, mobile later

  This shapes everything from UI style preferences to technical architecture, so
   I want to nail this before going further.
  ⎿  Stop says: Hookify import error: No module named 'hookify'

✻ Crunched for 18s

❯ Web MVP first, mobile later                                                   
  ⎿  UserPromptSubmit says: Hookify import error: No module named 'hookify'

⏺ Got it — web-first, with mobile as a follow-up phase.

  Next question: Who is the primary target user for Haute Food Fusion?

  - Home cooks — everyday people who cook for themselves or family, want to
  experiment with fun new dishes
  - Food enthusiasts / foodies — people who follow food culture, try new
  restaurants, and want to recreate "restaurant-quality" meals at home
  - Aspiring chefs / culinary students — people with serious interest in
  technique who want creative, challenging recipes
  - All of the above — the app serves multiple segments equally

  This will shape the personas section and how the skill level input is framed.
  ⎿  Stop says: Hookify import error: No module named 'hookify'

✻ Cooked for 6s

❯ All of the above                                                              
  ⎿  UserPromptSubmit says: Hookify import error: No module named 'hookify'

⏺ Good — that gives us three distinct personas to map journeys for.

  Next question: What is the intended monetization model?

  - Fully free — no paywalls, revenue comes later (ads, partnerships, etc.)
  - Freemium — free tier with limited generations/saves, paid tier for unlimited
   access
  - Subscription only — all features behind a monthly/annual fee
  - One-time purchase — pay once, access everything

  This directly affects the business success metrics and what we scope into MVP
  vs. later.
  ⎿  Stop says: Hookify import error: No module named 'hookify'

✻ Brewed for 5s

❯ Freemium                                                                      
  ⎿  UserPromptSubmit says: Hookify import error: No module named 'hookify'

⏺ Noted — freemium shapes both the business metrics and feature scoping
  significantly.

  Next question: For the freemium model, what would the free tier limits look 
  like?

  - Limited generations — e.g., 3 recipe generations per week, unlimited for
  paid
  - Limited saves — e.g., save up to 5 recipes for free, unlimited for paid
  - Both — limited generations AND limited saves on free tier
  - Feature-gated — free gets basic recipes, paid unlocks plating suggestions,
  ingredient substitutions, or other premium features

  This determines what we scope as core MVP vs. paid-only, and feeds directly
  into the business success metrics.
  ⎿  Stop says: Hookify import error: No module named 'hookify'

✻ Cooked for 9s

❯ Feature-gated                                                                 
  ⎿  UserPromptSubmit says: Hookify import error: No module named 'hookify'

⏺ Good — feature-gating creates a clear value ladder.

  Next question: Which specific features would be locked behind the paid tier?

  Given your current components (dish name, ingredients list, step-by-step
  recipe, plating suggestion), some natural options:

  - Plating suggestions — free gets the recipe, paid gets the high-end plating
  guidance
  - Recipe saving — free users can generate but not save; saving requires paid
  - Ingredient substitutions — paid users can request swaps (e.g., "I don't have
   X")
  - Export/print — paid users can export recipes as PDF or share links

  You don't have to pick from this list — you may have a different split in
  mind. What feels right to you as the free vs. paid divide?
  ⎿  Stop says: Hookify import error: No module named 'hookify'

✻ Cogitated for 9s

❯ Recipe saving, Ingredient substitutions, Export/print                         
  ⎿  UserPromptSubmit says: Hookify import error: No module named 'hookify'

⏺ Clear split — free users can generate and view full recipes including plating,
   but saving, substitutions, and exporting are paid.

  Next question: Should users be able to filter by dietary restrictions or 
  preferences?

  - Yes, in MVP — options like vegan, vegetarian, gluten-free, halal, kosher,
  nut-free, dairy-free
  - Yes, but post-MVP — important feature, but not needed for launch
  - No — the focus is purely on fusion creativity; dietary filtering is out of
  scope

  This is a meaningful scope decision — dietary filters add complexity to the AI
   prompt engineering and recipe validation logic.  ⎿  Stop says: Hookify import error: No module named 'hookify'

✻ Worked for 8s

❯ Yes, but post-MVP - important feature, but not needed for launch              
  ⎿  UserPromptSubmit says: Hookify import error: No module named 'hookify'

⏺ Noted — flagged for the post-MVP roadmap section.

  Next question: Is there a social or community element to the app?

  - No — recipes are private, purely a personal tool
  - Yes, in MVP — users can share recipes publicly or via link
  - Yes, but post-MVP — community features (likes, comments, recipe feeds) come
  later
  - Partially in MVP — users can share via a public link, but no social feed or
  profiles

  This affects whether we need user profiles, public recipe pages, and
  moderation considerations in the MVP.
  ⎿  Stop says: Hookify import error: No module named 'hookify'

✻ Churned for 5s

❯ Yes, in MVP - users can share recipes publicly or via link                    
  ⎿  UserPromptSubmit says: Hookify import error: No module named 'hookify'

⏺ Good — public sharing adds a meaningful social hook for growth and virality.

  Next question: How do users authenticate and manage accounts?

  - Email + password only — traditional sign-up flow
  - Social login only — Google, Apple, or similar (no password to manage)
  - Both — email/password AND social login options
  - No accounts on free tier — anonymous generation for free users, account
  required only for paid features

  This matters especially now that saving and sharing are in scope — both
  require some form of identity.
  ⎿  Stop says: Hookify import error: No module named 'hookify'

✻ Churned for 12s

❯ Both - email/password And social login options                                
  ⎿  UserPromptSubmit says: Hookify import error: No module named 'hookify'

⏺ Standard and flexible — good choice for maximizing sign-up conversion.

  Next question: What AI backend are you planning to use for recipe generation?

  - Claude (Anthropic API) — strong reasoning, nuanced instruction-following,
  great for creative culinary output
  - OpenAI (GPT-4/GPT-4o) — widely used, large ecosystem
  - Open to either / undecided — flexible, want the PRD to be AI-agnostic
  - Custom/fine-tuned model — planning to train or fine-tune on culinary data

  This shapes the technical considerations section, particularly around prompt
  engineering, rate limits, and cost modeling.
  ⎿  Stop says: Hookify import error: No module named 'hookify'

✻ Cogitated for 6s

❯ Claude (Anthropic API)                                                        
  ⎿  UserPromptSubmit says: Hookify import error: No module named 'hookify'

⏺ Excellent choice — Claude's instruction-following and creative reasoning make
  it well-suited for nuanced culinary generation.

  Next question: How do users select their cuisines — predefined list or 
  free-form input?

  - Predefined dropdown list — users pick from a curated set (e.g., Japanese,
  Mexican, French, Indian, etc.)
  - Free-form text input — users type any cuisine they want (more flexible, but
  harder to validate)
  - Both — dropdown with an "other" option for free-form entry
  - Tag-based search — users search and select tags from a large cuisine library

  This affects both UI design and how the AI prompt is structured — a predefined
   list makes it easier to ensure compatible, high-quality outputs.
  ⎿  Stop says: Hookify import error: No module named 'hookify'

✻ Cogitated for 5s

❯ Both — dropdown with an "other" option for free-form entry                    
  ⎿  UserPromptSubmit says: Hookify import error: No module named 'hookify'

⏺ Good — maximum flexibility while keeping structure for consistent AI outputs.

  Next question: What is the desired UI aesthetic for Haute Food Fusion?

  Given the "haute" branding and high-end plating suggestions, I want to
  understand the visual direction:

  - Elegant & minimal — dark backgrounds, gold/cream accents, editorial
  typography — feels like a Michelin-star restaurant menu
  - Warm & approachable — earthy tones, soft gradients, friendly typography —
  feels like a premium food magazine
  - Bold & modern — high contrast, vibrant food photography-style, strong type —
   feels like a trendy NYC pop-up
  - Clean & functional — white space, neutral palette, content-first — feels
  like a well-designed SaaS tool

  This directly feeds the UI style preferences section of the PRD.
  ⎿  Stop says: Hookify import error: No module named 'hookify'

✻ Cooked for 7s

❯ Elegant & minimal                                                             
  ⎿  UserPromptSubmit says: Hookify import error: No module named 'hookify'
⏺ Perfect — dark, editorial, and refined. That brand direction will inform the
  entire design language.

  Next question: How should skill levels be defined in the app?

  The app collects skill level as a user input, but the tiers need to mean
  something specific to the AI:

  - 3 tiers: Beginner / Intermediate / Advanced — simple and universal
  - 3 tiers with descriptions — e.g., "Home Cook (weeknight meals)" / "Confident
   Cook (techniques like braising, deboning)" / "Chef-Level (complex methods,
  specialty equipment)"
  - 5 tiers — more granular, e.g., Novice / Beginner / Intermediate / Advanced /
   Professional
  - Free-form self-description — users describe their own skill in their own
  words

  This directly shapes how the AI calibrates recipe complexity, technique
  language, and assumed equipment.
  ⎿  Stop says: Hookify import error: No module named 'hookify'

✻ Cogitated for 8s

❯ 3 tiers with descriptions                                                     
  ⎿  UserPromptSubmit says: Hookify import error: No module named 'hookify'

⏺ Good — descriptive tiers give Claude clear context to calibrate complexity,
  language, and technique appropriately.

  Next question: What makes Haute Food Fusion meaningfully different from 
  existing recipe apps like Yummly, ChefGPT, or DishGen?

  - The fusion angle — no other app specifically focuses on inventing original
  cross-cuisine dishes from scratch
  - The haute aesthetic — high-end plating guidance elevates it beyond
  utilitarian recipe tools
  - The AI creativity — it invents dishes that don't exist yet, not just
  searches a database
  - All of the above — the combination of fusion originality + high-end
  presentation + AI invention is the differentiator

  Understanding this sharpens the Problem Statement and competitive positioning
  in the PRD.
  ⎿  Stop says: Hookify import error: No module named 'hookify'

✻ Worked for 6s

❯ All of the above                                                              
  ⎿  UserPromptSubmit says: Hookify import error: No module named 'hookify'

⏺ Strong differentiator — the combination is the moat.

  Next question: Do you have a target timeline or launch date for the MVP?

  - ASAP / within 1-2 months — lean scope, ship fast, iterate
  - 3-6 months — room for polish and proper testing
  - 6-12 months — longer runway, higher quality bar before launch
  - No fixed timeline — quality over speed

  This helps calibrate how aggressively we scope the MVP and sets expectations
  in the technical considerations section.
  ⎿  Stop says: Hookify import error: No module named 'hookify'

✻ Crunched for 6s

❯ ASAP                                                                          
  ⎿  UserPromptSubmit says: Hookify import error: No module named 'hookify'

⏺ Noted — lean scope, fast ship. That will shape how we prioritize features in
  the MVP.

  Last question: How should recipe quality be validated before showing it to the
   user?

  Your success criteria include cookable recipes with realistic timing and
  compatible ingredients. The question is how strictly this is enforced:

  - AI prompt engineering only — Claude is instructed to self-validate; no
  secondary check
  - AI self-review pass — Claude generates the recipe, then a second prompt
  reviews it for timing, compatibility, and feasibility before returning it to
  the user
  - Human editorial review — a team member spot-checks generated recipes
  periodically
  - User feedback loop — users can flag bad recipes, which feeds back into
  improving prompts

  This is a meaningful technical and product decision — it affects latency,
  cost, and quality assurance.
  ⎿  Stop says: Hookify import error: No module named 'hookify'

✻ Churned for 11s

❯ AI self-review pass                                                           
  ⎿  UserPromptSubmit says: Hookify import error: No module named 'hookify'

⏺ That's all the clarification I need. Let me now write the full PRD.

  ★ Insight ─────────────────────────────────────
  A PRD is not a spec sheet — it's a shared contract between product, design,
  and engineering. The best PRDs answer three questions for every feature: what
  it does, why it matters, and how we know it's working. Keeping those three
  threads tight is what separates actionable PRDs from documents that get
  ignored.
  ─────────────────────────────────────────────────

  ---
  Haute Food Fusion — Product Requirements Document

  Version: 1.0
  Date: May 9, 2026
  Status: Draft

  ---
  1. Problem Statement

  Home cooks, food enthusiasts, and culinary students share a common
  frustration: they want to create exciting, original dishes that feel inventive
   and restaurant-worthy, but existing tools either search a static recipe
  database or produce generic AI-generated meals with no creative ambition.

  No product on the market specifically targets the growing appetite for fusion 
  cuisine creation — the act of deliberately blending two or more world cuisines
   into a single, coherent, original dish. Apps like Yummly surface existing
  recipes. ChefGPT and DishGen generate utilitarian meals. None combine the
  creative DNA of fusion cooking with the elevated aesthetic of high-end dining.

  Haute Food Fusion solves this by giving any cook — regardless of skill level —
   an AI-powered creative partner that invents original fusion dishes from
  scratch, tailored to the ingredients they already have, and presented with the
   visual and culinary language of a world-class restaurant.

  ---
  2. Business Success Metrics

  ┌──────────────────────┬───────────────────────────────┬─────────────────┐
  │        Metric        │            Target             │    Timeframe    │
  ├──────────────────────┼───────────────────────────────┼─────────────────┤
  │ Registered users     │ 1,000                         │ 30 days         │
  │                      │                               │ post-launch     │
  ├──────────────────────┼───────────────────────────────┼─────────────────┤
  │ Weekly Active Users  │ 40% of registered base        │ Ongoing         │
  │ (WAU)                │                               │                 │
  ├──────────────────────┼───────────────────────────────┼─────────────────┤
  │ Free → Paid          │ ≥ 5%                          │ 60 days         │
  │ conversion rate      │                               │ post-launch     │
  ├──────────────────────┼───────────────────────────────┼─────────────────┤
  │ Monthly Recurring    │ $2,000                        │ 90 days         │
  │ Revenue (MRR)        │                               │ post-launch     │
  ├──────────────────────┼───────────────────────────────┼─────────────────┤
  │ Recipe share rate    │ ≥ 15% of generated recipes    │ Ongoing         │
  │                      │ shared                        │                 │
  ├──────────────────────┼───────────────────────────────┼─────────────────┤
  │ Weekly return rate   │ ≥ 30% of users generate a new │ Ongoing         │
  │                      │  recipe each week             │                 │
  ├──────────────────────┼───────────────────────────────┼─────────────────┤
  │ Recipe save rate     │ ≥ 70% of paid users save at   │ Ongoing         │
  │ (paid users)         │ least 1 recipe/week           │                 │
  └──────────────────────┴───────────────────────────────┴─────────────────┘

  ▎ Virality note: Public recipe sharing is the primary organic growth lever. 
  ▎ Each shared recipe link is a free acquisition channel — track referral 
  ▎ signups from shared recipe pages.

  ---
  3. Personas & Key User Journeys

  Persona 1 — Maya, The Weekend Experimenter

  Profile: 34, home cook, cooks 4x/week, follows food influencers on Instagram.
  Has a decent pantry but no formal training. Wants to impress her partner with
  something creative on Friday night.
  Skill tier: Home Cook
  Goal: Turn random fridge ingredients into something fun and special without
  being overwhelmed.

  Journey:
  1. Maya lands on Haute Food Fusion via a shared recipe link from a friend.
  2. She creates a free account using Google login.
  3. She selects Japanese and Mexican from the cuisine dropdown.
  4. She types her available ingredients: chicken thighs, avocado, miso paste,
  lime, rice flour.
  5. She selects Home Cook skill level.
  6. She hits Generate — sees a loading state with a subtle animation.
  7. Claude returns: "Miso-Lime Pollo Tostada" — a dish name, full ingredients
  list, step-by-step instructions calibrated to her skill level, and a plating
  suggestion describing the dish as a high-end restaurant chef would.
  8. She loves it. She tries to save it — sees the paywall prompt: "Save 
  unlimited recipes with Haute Pro."
  9. She upgrades to paid, saves the recipe, and shares the public link with her
   sister.

  ---
  Persona 2 — Daniel, The Culinary Explorer

  Profile: 27, food enthusiast, eats out at 2-3 new restaurants per month,
  follows Michelin-star chefs on social media. Cooks ambitious weekend projects.
   Wants restaurant-quality outcomes at home.
  Skill tier: Confident Cook
  Goal: Create a dish that genuinely feels new and impressive — something he
  couldn't find on any menu.

  Journey:
  1. Daniel discovers Haute Food Fusion via a Reddit thread on AI cooking tools.
  2. He signs up with email and password.
  3. He selects French, Indian, and Peruvian — three cuisines he's been curious
  about combining.
  4. He lists: lamb shoulder, ghee, ají amarillo paste, herbes de Provence,
  fennel, coconut milk.
  5. He selects Confident Cook.
  6. Claude generates: "Ají Amarillo Agneau Confit" — a slow-braised lamb dish
  with a Peruvian-spiced French confit technique, served in a coconut-fennel
  jus, plated with microherb accents.
  7. Daniel is genuinely surprised by the originality. He saves the recipe and
  exports it as a PDF to print and reference while cooking.
  8. He shares the public recipe link on his food Instagram story. Three of his
  followers sign up.

  ---
  Persona 3 — Priya, The Craft-Focused Creator

  Profile: 22, culinary student, obsessed with technique and flavor theory. Uses
   cooking as creative expression. Wants complex, multi-component dishes that
  challenge her skills and vocabulary.
  Skill tier: Chef-Level
  Goal: Generate technically complex fusion recipes that use proper culinary
  terminology and push her abilities.

  Journey:
  1. Priya hears about Haute Food Fusion from her culinary school classmate.
  2. She signs up via Google and immediately upgrades to paid (wants saving from
   day one).
  3. She selects Korean and Italian.
  4. She inputs: short rib, doenjang, 00 flour, gochugaru, parmesan, kombu
  dashi, black truffle.
  5. She selects Chef-Level.
  6. Claude generates: "Doenjang Brasato with Gochugaru Pappardelle" — a
  technically demanding recipe with a doenjang-braised short rib ragù,
  hand-rolled gochugaru pasta, and a truffle-kombu dashi reduction. Instructions
   use terms like fond, emulsification, and al dente naturally.
  7. She requests an ingredient substitution: "I don't have black truffle."
  Claude suggests porcini powder as a umami-forward alternative.
  8. She saves, exports, and returns every week to generate new dishes for her
  portfolio.

  ---
  4. Technical Success Metrics

  ┌───────────────────────────────────────────────────────────┬─────────────┐
  │                          Metric                           │   Target    │
  ├───────────────────────────────────────────────────────────┼─────────────┤
  │ End-to-end recipe generation latency (generate +          │ ≤ 12        │
  │ self-review pass)                                         │ seconds     │
  ├───────────────────────────────────────────────────────────┼─────────────┤
  │ Claude API self-review pass rate (first attempt)          │ ≥ 90%       │
  ├───────────────────────────────────────────────────────────┼─────────────┤
  │ Recipe generation error rate                              │ ≤ 1%        │
  ├───────────────────────────────────────────────────────────┼─────────────┤
  │ Authentication success rate                               │ ≥ 99%       │
  ├───────────────────────────────────────────────────────────┼─────────────┤
  │ App uptime                                                │ ≥ 99.5%     │
  ├───────────────────────────────────────────────────────────┼─────────────┤
  │ Public share page load time                               │ ≤ 2 seconds │
  ├───────────────────────────────────────────────────────────┼─────────────┤
  │ Paywall conversion prompt click-through rate              │ ≥ 20%       │
  └───────────────────────────────────────────────────────────┴─────────────┘

  ---
  5. Scope of MVP

  In Scope

  Authentication
  - Email + password sign-up and login
  - Google OAuth and Apple Sign-In
  - Password reset flow

  Recipe Generation
  - Cuisine selector: dropdown of ~50 world cuisines + free-form "Other" field
  - Ingredient input: free-text field (comma-separated or line-by-line)
  - Skill level selector: 3 tiers with descriptions
    - Home Cook — "I handle weeknight meals; comfortable with sautéing, boiling,
   basic techniques"
    - Confident Cook — "I'm comfortable with braising, deboning, making sauces
  from scratch"
    - Chef-Level — "I can tackle complex methods, multi-component dishes, and
  specialty equipment"
  - AI generation via Claude API (two-pass: generate → self-review for
  cookability, timing, and ingredient compatibility)
  - Output: unique dish name, ingredients list, step-by-step recipe, plating
  suggestion

  Freemium Gating
  - Free tier: unlimited recipe generation and viewing (including plating
  suggestions), public sharing via link
  - Paid tier (Haute Pro): recipe saving, ingredient substitutions, export/print
   as PDF
  - Paywall prompt surfaced contextually when free users attempt paid actions
  - Stripe integration for subscription billing

  Sharing
  - Every generated recipe gets a unique public URL
  - Public recipe pages are accessible without an account (view only)
  - Copy link CTA on recipe output page

  User Account
  - Saved recipes library (paid users)
  - Basic profile page

  Out of Scope (Post-MVP)

  - Mobile app (iOS / Android)
  - Dietary restriction filters (vegan, gluten-free, halal, etc.)
  - Community feed, likes, comments, following
  - Recipe ratings or user reviews
  - Ingredient quantity scaling
  - Wine or beverage pairing suggestions
  - Multi-language support

  ---
  6. Technical Considerations

  AI Architecture

  - Model: Claude claude-sonnet-4-6 (Anthropic API) — balances quality and cost
  at MVP scale
  - Two-pass generation pattern:
    - Pass 1: Generate the full recipe (dish name, ingredients, method, plating)
    - Pass 2: Self-review prompt instructs Claude to evaluate its own output
  against three criteria: realistic timing, ingredient compatibility, and
  skill-level appropriateness — then revise if needed
  - Prompt engineering: Cuisine inputs, skill level descriptions, and available
  ingredients are injected into a structured system prompt. The prompt must
  constrain Claude to invent original dishes (not reproduce known dishes), use
  only provided ingredients as primary components, and maintain the high-end
  naming and plating language consistent with the brand
  - Prompt caching: Use Anthropic's prompt caching on the static system prompt
  portion to reduce latency and cost on repeat generations
  - Ingredient substitution: Implemented as a follow-up Claude call in context,
  referencing the original recipe — not a fresh generation

  Authentication

  - Provider: Supabase Auth or Auth.js — supports email/password + OAuth
  providers natively
  - Session management: JWT-based, server-side validation

  Database

  - Saved recipes: Stored in PostgreSQL (via Supabase or PlanetScale) — recipe
  JSON blob, user ID, timestamps, public share token
  - Public share tokens: UUID-based, generated at recipe creation time
  regardless of tier (free users can share even without saving)

  Payments

  - Provider: Stripe — subscription billing, webhook handling for
  upgrade/downgrade/cancellation
  - Paywall enforcement: Server-side feature flag check on save, substitute, and
   export endpoints

  Hosting

  - Frontend: Vercel (Next.js) — fast deployment, edge rendering for public
  recipe pages
  - Backend: Vercel serverless functions or a lightweight Node/Express API layer

  Rate Limiting

  - Free tier: no generation limits in MVP (feature-gated, not quantity-gated) —
   revisit if API costs spike
  - Paid tier: no limits
  - Implement per-IP and per-user rate limiting on the generation endpoint to
  prevent abuse

  ---
  7. UI Style Preferences

  Aesthetic Direction: Elegant & minimal — the visual language of a
  Michelin-star restaurant menu, not a recipe blog.

  ┌───────────────┬─────────────────────────────────────────────────────────┐
  │    Element    │                        Direction                        │
  ├───────────────┼─────────────────────────────────────────────────────────┤
  │ Color palette │ Dark background (near-black #0D0D0D or deep charcoal),  │
  │               │ gold/cream accents (#C9A84C, #F5F0E8), white text       │
  ├───────────────┼─────────────────────────────────────────────────────────┤
  │               │ Serif display font for dish names and headings (e.g.,   │
  │ Typography    │ Playfair Display, Cormorant Garamond); clean sans-serif │
  │               │  for body and UI (e.g., Inter, DM Sans)                 │
  ├───────────────┼─────────────────────────────────────────────────────────┤
  │ Layout        │ Generous white space, single-column recipe output, no   │
  │               │ visual clutter                                          │
  ├───────────────┼─────────────────────────────────────────────────────────┤
  │               │ No stock food photography — let the recipe and plating  │
  │ Imagery       │ language do the visual work; consider subtle            │
  │               │ food-texture backgrounds or abstract dark gradients     │
  ├───────────────┼─────────────────────────────────────────────────────────┤
  │               │ Subtle fade-in animations on recipe reveal; smooth      │
  │ Interactions  │ loading state during generation (e.g., animated         │
  │               │ wordmark or pulsing gold line)                          │
  ├───────────────┼─────────────────────────────────────────────────────────┤
  │ Recipe output │ Dish name in large serif, plating suggestion styled     │
  │  card         │ distinctly (italic, gold accent bar) to feel like       │
  │               │ editorial food writing                                  │
  ├───────────────┼─────────────────────────────────────────────────────────┤
  │ Paywall       │ Non-aggressive, elegant modal — framed as an invitation │
  │ prompt        │  to "unlock the full experience," not a hard block      │
  └───────────────┴─────────────────────────────────────────────────────────┘

  ---
  8. Corner Cases

  Input Edge Cases

  Scenario: User selects fewer than 2 cuisines
  Handling: Inline validation: "Please select at least 2 cuisines to create a
    fusion dish." Block generation.
  ────────────────────────────────────────
  Scenario: User selects more than 3 cuisines
  Handling: Cap the selector at 3 with a tooltip: "Fusion works best with 2-3
    cuisines for coherent flavor profiles."
  ────────────────────────────────────────
  Scenario: Free-form cuisine input is not a real cuisine
  Handling: Claude's system prompt is instructed to flag unrecognized cuisines
    and ask for clarification in the output, or gracefully interpret closest
    match
  ────────────────────────────────────────
  Scenario: User submits empty or near-empty ingredient list
  Handling: Prompt validation: require at least 3 ingredients. Show helper text:

    "Add at least 3 ingredients for a meaningful fusion."
  ────────────────────────────────────────
  Scenario: Ingredients are incompatible or incoherent (e.g., "ice cream, raw
    fish, vinegar")
  Handling: Self-review pass catches this and either revises the recipe or flags

    a warning in the output: "Note: some ingredient combinations were adjusted
    for culinary compatibility."
  ────────────────────────────────────────
  Scenario: User inputs an extremely long ingredient list (50+ items)
  Handling: Truncate to first 20 ingredients with a note: "We've focused on your

    top 20 ingredients for the best results."

  Generation Edge Cases

  ┌──────────────────────┬──────────────────────────────────────────────────┐
  │       Scenario       │                     Handling                     │
  ├──────────────────────┼──────────────────────────────────────────────────┤
  │                      │ Return the best available result with a soft     │
  │ Self-review pass     │ disclaimer: "This recipe is experimental — use   │
  │ fails twice          │ your best judgement on timing." Log failure for  │
  │                      │ prompt tuning.                                   │
  ├──────────────────────┼──────────────────────────────────────────────────┤
  │ Claude API timeout   │ Show a user-friendly error state with retry CTA. │
  │ or error             │  Do not expose raw API errors.                   │
  ├──────────────────────┼──────────────────────────────────────────────────┤
  │ Claude reproduces a  │ Self-review prompt explicitly checks for this    │
  │ well-known existing  │ and instructs a rename/modification if the dish  │
  │ dish                 │ name matches a known recipe                      │
  ├──────────────────────┼──────────────────────────────────────────────────┤
  │ Identical inputs     │ Inject a randomness seed or variation            │
  │ generate the same    │ instruction into the prompt to ensure creative   │
  │ recipe repeatedly    │ variation across generations                     │
  └──────────────────────┴──────────────────────────────────────────────────┘

  Auth & Account Edge Cases

  ┌───────────────────────────┬─────────────────────────────────────────────┐
  │         Scenario          │                  Handling                   │
  ├───────────────────────────┼─────────────────────────────────────────────┤
  │ User tries to sign up     │ Surface clear error: "This email is linked  │
  │ with email already linked │ to a Google account. Sign in with Google."  │
  │  to Google OAuth          │                                             │
  ├───────────────────────────┼─────────────────────────────────────────────┤
  │ Unauthenticated user      │ Full recipe is visible (read-only). Sticky  │
  │ accesses a public recipe  │ CTA bar: "Create your own fusion dish free  │
  │ share link                │ →"                                          │
  ├───────────────────────────┼─────────────────────────────────────────────┤
  │ Free user attempts to     │ Trigger paywall modal immediately, preserve │
  │ save a recipe             │  the recipe in session so it's not lost if  │
  │                           │ user upgrades                               │
  ├───────────────────────────┼─────────────────────────────────────────────┤
  │                           │ Saved recipes remain accessible             │
  │ Paid subscription lapses  │ (read-only). Generation still works.        │
  │ mid-session               │ Save/export/substitute actions prompt       │
  │                           │ re-subscription.                            │
  └───────────────────────────┴─────────────────────────────────────────────┘

  Sharing Edge Cases

  ┌─────────────────────┬───────────────────────────────────────────────────┐
  │      Scenario       │                     Handling                      │
  ├─────────────────────┼───────────────────────────────────────────────────┤
  │ Public recipe link  │ Public URL is generated at generation time        │
  │ is shared before    │ regardless — share token is tied to the recipe    │
  │ user saves (free    │ session, not a saved record. Recipe is accessible │
  │ tier)               │  via link for 30 days without saving.             │
  ├─────────────────────┼───────────────────────────────────────────────────┤
  │ User deletes their  │ Public recipe share links from that user become   │
  │ account             │ anonymized ("Recipe by a Haute Food Fusion user") │
  │                     │  rather than broken.                              │
  └─────────────────────┴───────────────────────────────────────────────────┘

  ---
  ★ Insight ─────────────────────────────────────
  The two-pass Claude self-review pattern is a form of LLM-as-judge — using the
  model to evaluate its own outputs before they reach the user. This costs
  roughly 2x the tokens of a single pass but dramatically reduces hallucinated
  timing, incoherent ingredient pairings, and skill-level mismatches. For a
  product where recipe quality is the core trust signal, it's worth the latency
  trade-off.
  ─────────────────────────────────────────────────

  ---
  That's the complete PRD. A few things worth flagging for your next
  conversation with an engineer or designer:

  1. The 30-day public link expiry for unsaved free-tier recipes is a judgment
  call — you may want to make it permanent to maximize virality.
  2. Prompt caching on the Claude API system prompt will meaningfully reduce
  cost as generation volume scales.
  3. The dietary restriction post-MVP decision is the right call for speed, but
  you'll want to revisit it early — it's the most common user request you'll
  likely receive after launch.
  ⎿  Stop says: Hookify import error: No module named 'hookify'

✻ Baked for 2m 12s