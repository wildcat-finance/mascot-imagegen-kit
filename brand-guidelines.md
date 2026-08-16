## Master brand prompt

> Create a branded visual for Wildcat Protocol, an on-chain undercollateralized credit platform. The visual should feel precise, secure, modern, technically credible, and slightly unconventional.
>
> Use a clean editorial-fintech aesthetic with generous negative space, strong hierarchy, restrained detail, and simple geometric construction. Favor near-black, deep plum, purple, ultramarine blue, muted red, and coral gradients. Gradients should be atmospheric and dimensional, with soft blurred transitions, dark edges, and localized areas of color rather than uniform rainbow blending.
>
> Suitable motifs include subtle perspective grids, abstract credit networks, connected market structures, restrained protocol diagrams, minimal interface-inspired cards, and the Wildcat mascot.
>
> When the mascot appears, use the images in `./assets` as visual references. Preserve the mascot’s recognizable angular head, tall pointed ears, narrow yellow eyes, light grey or white colouring, lean proportions, and reserved, intelligent expression. Treat the references as the source of truth for the character’s identity. Adapt the pose, clothing, setting, and rendering style as required, but do not redesign the character or turn it into a generic cat, fox, or human-animal hybrid. Ignore captions or text contained in the reference images unless explicitly requested.
>
> Keep compositions uncluttered and suitable for institutional financial communications. Provide clear empty space for headlines and the official Wildcat logo to be added later.
>
> Do not generate text or recreate the Wildcat logo. Do not use generic cryptocurrency symbols, coins, token stacks, circuit-board patterns, glowing blockchain cubes, cyberpunk cityscapes, excessive neon, glossy 3D graphics, stock photography, or crowded dashboards.

## Core visual rules

* Primary dark: Bunker `#141414`
* Supporting dark: Black Rock `#30313E`
* Primary blue: Ultramarine Blue `#3E68FF`
* Supporting blues: `#4971FF`, `#6688FF`
* Primary purple: Purple Heart `#4D26BC`
* Supporting purple: Light Slate Blue `#7D71FF`
* Warm accents: Dull Red `#C24647`, Carmine Pink `#F1464B`, Wild Watermelon `#FA6F77`
* Light backgrounds: `#F4F4F8`, `#F6F6F7`, `#F9F9FA`, `#FCFCFC`
* Use yellow mainly for warnings or status communication.
* Use red for risk, urgency, errors, or controlled warm-gradient accents.
* Prefer black-and-white logo applications.
* Add the official logo as a supplied asset after generation.
* Whenever the mascot appears, reference the source images in `./assets`.

Typography should be applied during layout rather than generated into images:

* Headlines: Liberation Sans
* Body and interface text: Inter
* Headlines should be bold, direct, and relatively large.
* Body copy should be neutral, legible, and informational.

## Prompt scaffold

> Create a `[format and dimensions]` Wildcat Protocol visual about `[subject]`.
>
> Style: modern institutional DeFi, clean editorial composition, technically precise, secure, minimal, slightly irreverent.
>
> Composition: `[subject placement]`, generous negative space in `[location]` for typography, strong geometric hierarchy, minimal visual elements.
>
> Color: near-black `#141414`, deep plum, Purple Heart `#4D26BC`, Ultramarine Blue `#3E68FF`, with restrained Dull Red `#C24647` or coral `#FA6F77` accents.
>
> Visual treatment: atmospheric blurred gradient, subtle perspective grid or fine-line protocol structure, crisp edges, restrained depth, no decorative clutter.
>
> Mascot: `[include or omit]`. If included, use the images in `./assets` as character references and preserve the established character identity. Ignore reference-image captions and backgrounds unless requested.
>
> Output: no text, letters, logos, or watermarks. Leave the designated copy area visually quiet.

## Hero-background prompt

> Create a 16:9 hero background for Wildcat Protocol. Show an abstract representation of on-chain credit infrastructure through a subtle receding grid and a small number of precise interconnected lines. Dark near-black and plum edges transition into concentrated ultramarine and purple, with a restrained red-coral glow on one side. Sophisticated institutional-finance atmosphere, secure and technically credible, soft depth, controlled contrast, and minimal detail. Leave the left-center area quiet for a large white headline. No mascot, text, logo, coins, chains, cubes, circuitry, or cyberpunk imagery.

## Mascot-led hero prompt

> Create a 16:9 Wildcat Protocol hero image featuring the Wildcat mascot. Use the images in `./assets` as visual references and preserve the same character identity, including the angular head, tall pointed ears, narrow yellow eyes, light grey-white colouring, lean proportions, and restrained intelligent expression.
>
> Show the mascot `[action or scenario]`. Place the character on the right third of the composition, leaving a large quiet area on the left for a headline. Use a dark plum-to-purple background with restrained ultramarine and red-coral light, a subtle perspective grid, and minimal financial-network details. Modern institutional DeFi aesthetic, technically credible and slightly irreverent.
>
> Ignore captions, text, interfaces, and backgrounds from the reference images. Do not redesign the mascot. No generated text, logo, coins, blockchain cubes, cyberpunk effects, or glossy cartoon rendering.

## Editorial campaign prompt

> Create a bold editorial Wildcat Protocol visual representing flexible credit terms replacing rigid lending structures. Show two contrasting abstract systems: one rigid and repetitive, the other open and adaptable. Optionally include the Wildcat mascot observing or disrupting the rigid system; if included, use `./assets` as the character reference.
>
> Use simple geometric forms, thin technical lines, generous negative space, near-black, purple, ultramarine, and a restrained warm-red accent. Clean, intelligent, slightly provocative, and suitable for an institutional DeFi campaign. Flat-to-dimensional hybrid style, not glossy 3D. No text or logo.

## Mascot illustration prompt

> Create an illustration of the Wildcat mascot explaining `[financial concept]`. Use the images in `./assets` as visual references and preserve the established facial structure, ears, eyes, proportions, and overall identity.
>
> Render the character as sparse monochrome editorial line art with thin near-black outlines and economical construction. The expression should feel intelligent, dry, and slightly mischievous rather than cute or childish. Place the character on a warm-white or very light-grey background with ample negative space. Use one restrained blue or pale-purple technical accent if needed.
>
> Ignore captions, backgrounds, clothing, and other characters in the reference images unless explicitly requested. No photorealism, fur texture, glossy 3D rendering, text, or logo.

## Protocol-diagram prompt

> Create a minimal conceptual diagram showing direct credit flowing between a borrower and a lender. Use two simple rounded rectangular nodes, thin near-black outlines, a restrained bidirectional connector, and faint overlapping blue and purple orbital lines behind the nodes. White or off-white background, precise fintech interface aesthetic, sparse composition, substantial negative space. No mascot, labels, numbers, logos, blockchain icons, coins, or decorative complexity.

## Social-graphic prompt

> Create a square Wildcat Protocol social visual about `[topic]`. Use a dark plum-to-purple-to-muted-red atmospheric gradient with a subtle perspective grid.
>
> Include the Wildcat mascot using the images in `./assets` as visual references. Show the character `[pose or action]`, maintaining its established angular anatomy and restrained intelligent personality. Ignore any existing captions or backgrounds in the references.
>
> Use a strong central or off-centre composition with ample high-contrast space for a short headline. Modern institutional-finance aesthetic. No generated text, logo, token imagery, glassmorphism, or excessive glow.

## Negative prompt

> Generic crypto aesthetic, Bitcoin or Ethereum coins, token stacks, chains, blockchain cubes, hexagon networks, circuitry, cyberpunk city, hacker imagery, holograms, excessive neon, rainbow gradients, lens flares, glossy glassmorphism, chrome 3D objects, generic cats, foxes, cute furry mascots, human faces with cat ears, stock-photo executives, crowded dashboards, illegible UI, generated words, fake logos, captions, or watermarks.
