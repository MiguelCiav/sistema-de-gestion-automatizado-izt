---
name: Terra Lab Design System
colors:
  surface: '#f7faf7'
  surface-dim: '#d8dbd8'
  surface-bright: '#f7faf7'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f4f1'
  surface-container: '#ecefeb'
  surface-container-high: '#eae6de'
  surface-container-highest: '#e0e3e0'
  on-surface: '#181c1b'
  on-surface-variant: '#414942'
  inverse-surface: '#2d312f'
  inverse-on-surface: '#eef1ee'
  outline: '#717971'
  outline-variant: '#c1c9bf'
  surface-tint: '#376847'
  primary: '#316342'
  on-primary: '#ffffff'
  primary-container: '#78a886'
  on-primary-container: '#e1ffe5'
  inverse-primary: '#9dd3aa'
  secondary: '#655d52'
  on-secondary: '#ffffff'
  secondary-container: '#e9ded0'
  on-secondary-container: '#696156'
  tertiary: '#6a572b'
  on-tertiary: '#ffffff'
  tertiary-container: '#846f41'
  on-tertiary-container: '#fff6ec'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#b9efc5'
  primary-fixed-dim: '#9dd3aa'
  on-primary-fixed: '#00210e'
  on-primary-fixed-variant: '#1e5031'
  secondary-fixed: '#ece1d3'
  secondary-fixed-dim: '#d0c5b8'
  on-secondary-fixed: '#201b12'
  on-secondary-fixed-variant: '#4d463c'
  tertiary-fixed: '#fbdfa8'
  tertiary-fixed-dim: '#dec38e'
  on-tertiary-fixed: '#251a00'
  on-tertiary-fixed-variant: '#56441b'
  background: '#f7faf7'
  on-background: '#181c1b'
  surface-variant: '#e0e3e0'
  surface-warm: '#faf6f0'
  success-green: '#4a7c59'
  error-red: '#b83230'
typography:
  display-lg:
    fontFamily: Literata
    fontSize: 60px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: Literata
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-xl-mobile:
    fontFamily: Literata
    fontSize: 36px
    fontWeight: '700'
    lineHeight: '1.2'
  title-lg:
    fontFamily: Literata
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Nunito Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Nunito Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-lg:
    fontFamily: Nunito Sans
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.2'
  label-sm:
    fontFamily: Nunito Sans
    fontSize: 10px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 48px
  xl: 64px
  container-max: 448px
---

## Brand & Style
Terra Lab embodies a "Natural Precision" aesthetic—merging the sterile, methodical nature of a laboratory with the organic, warm tones of the earth. The brand personality is professional and trustworthy yet approachable and calm, moving away from the cold blues typically associated with science and tech.

The design style is **Corporate Modern with Tactile influences**. It utilizes a "soft-professional" approach: clean layouts and systematic grids paired with organic color palettes and significant roundedness. Subtle rotations and layered surfaces (as seen in the logo container) provide a sense of depth and physical presence without leaning into heavy skeuomorphism. The interface aims to evoke a feeling of "scientific clarity" through generous white space and high-quality serif typography.

## Colors
The palette is rooted in an "Earth-Tonal" spectrum. 
- **Primary Green (#4a7c59):** Represents growth and organic chemistry; used for primary actions and active states.
- **Secondary Taupe (#6b6358):** A grounding neutral-warm used for supporting text and icons.
- **Tertiary Gold/Ochre (#705c30):** Used sparingly for accents and highlights.
- **Surface Warm (#faf6f0):** Instead of pure white, a cream-tinted background reduces eye strain and reinforces the organic brand feel.

Contrast is maintained through a deep charcoal neutral (#2e3230) for text, ensuring accessibility while remaining softer than pure black.

## Typography
The system uses a sophisticated pairing of **Literata** (Serif) and **Nunito Sans** (Sans-Serif). 

- **Literata** is reserved for headlines and branding. Its bookish, scholarly character reinforces the "Lab" and "Research" aspects of the product. Large displays should use a tight letter-spacing for a modern editorial look.
- **Nunito Sans** is used for all functional text, inputs, and body copy. Its slightly rounded terminals complement the overall shape language and maintain high legibility in dense data environments.
- **Scale:** On mobile devices, headline sizes scale down significantly (e.g., 48px to 36px) to ensure content remains the primary focus without excessive scrolling.

## Layout & Spacing
The layout follows a **Fixed Center-Column** philosophy for setup and transactional flows, transitioning to a fluid grid for data-heavy dashboards.

- **Margins:** Mobile views utilize a 24px (md) side margin. Desktop layouts constrain the main content to a "container-max" of 448px for focused setup tasks.
- **Rhythm:** Vertical spacing is generous (48px - 64px between major sections) to create an unhurried, step-by-step atmosphere.
- **Responsive Behavior:** On mobile, navigation is anchored to the bottom using a high-elevation BottomAppBar. On desktop, navigation shifts to a persistent top bar or side rail.

## Elevation & Depth
The system uses **Tonal Layers** and **Ambient Shadows** to define hierarchy.

- **Layering:** Backgrounds use the lightest `surface-warm`. Elements like cards or secondary containers use `surface-container-high` to create visual "steps."
- **Shadows:** Shadows are highly diffused and tinted with the neutral-charcoal color (e.g., `rgba(46, 50, 48, 0.15)`). They are used primarily on floating action buttons and active navigation elements to suggest interactivity.
- **Logo Graphic Depth:** Uses a "stacked deck" effect with slight rotations (-2 to 3 degrees) and varying opacities to create a tactile, paper-like feel.

## Shapes
The shape language is consistently **Rounded (Level 2)**.
- **Buttons & Inputs:** Use `rounded-xl` (1.5rem) for a friendly, modern feel that invites interaction.
- **Progress Indicators:** Small elements like step indicators use circular (full) rounding.
- **Containers:** Large cards and surface containers use `rounded-2xl` or specific custom values (like 2rem for the logo container) to emphasize the soft-professional aesthetic.

## Components
- **Buttons:** Primary buttons are large, high-contrast blocks with `primary` background and `on-primary` text. They should feature a hover state that slightly elevates (-4px translate) and a subtle glow shadow.
- **Progress Steppers:** Use a combination of a background line (`surface-variant`) and an active line (`primary`). Completed steps are indicated with a filled circle and checkmark, while the active step uses a `primary-container` fill with a double-ring border.
- **Bottom Navigation:** Mobile navigation features large icons with small, capitalized labels. The active state is highlighted with a pill-shaped container (`primary-container`).
- **Cards:** Cards should be flat or use very low-contrast outlines (`outline-variant/30`) to avoid visual clutter, relying on spacing and tonal changes for separation.
- **Inputs:** (Extended) Should follow the same 1.5rem rounding as buttons, with labels in `Nunito Sans` Bold 14px above the field.