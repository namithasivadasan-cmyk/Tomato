# Python script to generate the complete, enhanced Tomato web app with:
# 1. Games & Spin Wheel (Discounts & Rare Prizes + Mini Arcade)
# 2. Train Delivery & Theater Delivery (Train No, Station, Coach, Berth, Multiplex, Audi, Seat No)
# 3. Multiple Funny Cartoon Goat Images at the end with Real Goat Sound Effect & Soundboard

import os

app_html = '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tomato 🍅 — Delivering to Doorstep, Trains & Theaters | Zomato Parody</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800;900&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <style>
        :root {
            --tomato-red: #E23744;
            --tomato-dark: #C82333;
            --tomato-glow: rgba(226, 55, 68, 0.25);
            --charcoal: #1C1C1C;
            --text-main: #1F2937;
            --text-muted: #6B7280;
            --text-light: #9CA3AF;
            --bg-page: #F8F9FA;
            --bg-white: #FFFFFF;
            --border-color: #E5E7EB;
            --veg-green: #24963F;
            --veg-light: #EBF8EE;
            --nonveg-red: #E43B4F;
            --nonveg-light: #FDECEE;
            --star-gold: #F4A213;
            --badge-bg: #F4F5F7;
            --train-blue: #0284C7;
            --cinema-purple: #7C3AED;
            --gold-gradient: linear-gradient(135deg, #FFD700 0%, #FFA500 50%, #FF8C00 100%);
            --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.06);
            --shadow-md: 0 6px 18px rgba(0, 0, 0, 0.08);
            --shadow-lg: 0 12px 32px rgba(0, 0, 0, 0.12);
            --shadow-red: 0 8px 24px rgba(226, 55, 68, 0.35);
            --radius-sm: 8px;
            --radius-md: 14px;
            --radius-lg: 20px;
            --radius-full: 999px;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: var(--bg-page);
            color: var(--text-main);
            line-height: 1.5;
            overflow-x: hidden;
            min-height: 100vh;
        }

        h1, h2, h3, h4, .brand-font {
            font-family: 'Outfit', sans-serif;
        }

        button {
            font-family: inherit;
            cursor: pointer;
            border: none;
            outline: none;
            transition: all 0.2s ease;
        }

        a {
            text-decoration: none;
            color: inherit;
        }

        /* ---------------- TOP ANNOUNCEMENT STRIP ---------------- */
        .scratch-announcement-strip {
            background: linear-gradient(90deg, #18181B 0%, #311803 25%, #854D0E 60%, #18181B 100%);
            color: #FFF;
            padding: 10px 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 14px;
            font-size: 13.5px;
            font-weight: 700;
            position: relative;
            z-index: 101;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
            flex-wrap: wrap;
        }

        .scratch-strip-badge {
            background: #F59E0B;
            color: #000;
            padding: 3px 10px;
            border-radius: var(--radius-full);
            font-size: 11.5px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            animation: pulseGlow 1.5s infinite;
        }

        @keyframes pulseGlow {
            0%, 100% { transform: scale(1); box-shadow: 0 0 0 rgba(245, 158, 11, 0.7); }
            50% { transform: scale(1.05); box-shadow: 0 0 14px rgba(245, 158, 11, 0.9); }
        }

        .scratch-strip-cta {
            background: #FFF;
            color: #1C1C1C;
            padding: 5px 14px;
            border-radius: var(--radius-full);
            font-size: 12px;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 5px;
        }
        .scratch-strip-cta:hover {
            background: #FCD34D;
            transform: scale(1.04);
        }

        /* ---------------- HEADER & NAVIGATION ---------------- */
        .top-header {
            position: sticky;
            top: 0;
            z-index: 100;
            background: rgba(255, 255, 255, 0.96);
            backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border-color);
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.03);
        }

        .header-inner {
            max-width: 1260px;
            margin: 0 auto;
            padding: 12px 20px;
            display: flex;
            align-items: center;
            gap: 16px;
        }

        .logo-box {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 28px;
            font-weight: 800;
            color: var(--tomato-red);
            letter-spacing: -0.5px;
            cursor: pointer;
            user-select: none;
            flex-shrink: 0;
        }

        .logo-box span.logo-sub {
            font-size: 11px;
            background: #FFE5E7;
            color: var(--tomato-red);
            font-weight: 700;
            padding: 2px 7px;
            border-radius: var(--radius-full);
            vertical-align: middle;
            margin-left: 2px;
            letter-spacing: 0.5px;
        }

        /* Search & Location Bar */
        .search-locality-wrap {
            flex: 1;
            display: flex;
            align-items: center;
            background: var(--bg-white);
            border: 1.5px solid #E2E8F0;
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-sm);
            overflow: hidden;
            height: 48px;
            transition: all 0.2s;
        }

        .search-locality-wrap:focus-within {
            border-color: var(--tomato-red);
            box-shadow: 0 0 0 3px var(--tomato-glow);
        }

        .locality-selector {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 0 14px;
            min-width: 190px;
            border-right: 1px solid #EBEBEB;
            color: var(--text-main);
            font-size: 13.5px;
            font-weight: 700;
            background: #F8FAFC;
            height: 100%;
            cursor: pointer;
        }

        .locality-selector select {
            border: none;
            background: transparent;
            outline: none;
            font-family: inherit;
            font-weight: 700;
            color: var(--text-main);
            cursor: pointer;
            width: 100%;
        }

        .search-input-box {
            flex: 1;
            display: flex;
            align-items: center;
            padding: 0 14px;
            gap: 10px;
            height: 100%;
        }

        .search-input-box input {
            border: none;
            outline: none;
            width: 100%;
            font-family: inherit;
            font-size: 14px;
            color: var(--text-main);
        }

        /* Header Action Buttons */
        .header-actions {
            display: flex;
            align-items: center;
            gap: 10px;
            flex-shrink: 0;
        }

        .games-header-btn {
            background: linear-gradient(135deg, #FF6B6B 0%, #EE5253 50%, #FF9F43 100%);
            color: white;
            padding: 8px 14px;
            border-radius: var(--radius-full);
            font-size: 13px;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 6px;
            box-shadow: 0 4px 12px rgba(238, 82, 83, 0.35);
            animation: softBounce 2s infinite;
        }

        @keyframes softBounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-2px); }
        }

        .mode-header-badge {
            background: #F1F5F9;
            border: 1px solid #CBD5E1;
            padding: 7px 12px;
            border-radius: var(--radius-full);
            font-size: 12.5px;
            font-weight: 700;
            color: var(--charcoal);
            display: flex;
            align-items: center;
            gap: 6px;
            cursor: pointer;
            transition: all 0.2s;
        }
        .mode-header-badge:hover {
            border-color: var(--tomato-red);
            background: #FFF1F2;
        }

        .cart-btn-main {
            background: var(--tomato-red);
            color: white;
            padding: 9px 18px;
            border-radius: var(--radius-full);
            font-size: 14px;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 4px 14px rgba(226, 55, 68, 0.3);
            position: relative;
        }
        .cart-btn-main:hover {
            background: var(--tomato-dark);
            transform: translateY(-1px);
        }

        .cart-badge-count {
            background: white;
            color: var(--tomato-red);
            font-size: 11px;
            font-weight: 800;
            padding: 2px 7px;
            border-radius: var(--radius-full);
        }

        /* ---------------- DELIVERY MODE SELECTOR SECTION ---------------- */
        .delivery-modes-strip {
            background: #FFFFFF;
            border-bottom: 1px solid #E2E8F0;
            padding: 14px 20px;
        }

        .delivery-modes-container {
            max-width: 1260px;
            margin: 0 auto;
        }

        .mode-tabs-bar {
            display: flex;
            align-items: center;
            gap: 12px;
            overflow-x: auto;
            padding-bottom: 4px;
        }

        .mode-tab-btn {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px 18px;
            border-radius: var(--radius-md);
            font-size: 13.5px;
            font-weight: 800;
            border: 2px solid #E2E8F0;
            background: #F8FAFC;
            color: #475569;
            transition: all 0.2s ease;
            white-space: nowrap;
        }

        .mode-tab-btn:hover {
            border-color: #CBD5E1;
            background: #FFFFFF;
            transform: translateY(-1px);
        }

        .mode-tab-btn.active.mode-doorstep {
            border-color: var(--tomato-red);
            background: #FFF5F5;
            color: var(--tomato-red);
            box-shadow: 0 4px 12px rgba(226, 55, 68, 0.15);
        }

        .mode-tab-btn.active.mode-train {
            border-color: var(--train-blue);
            background: #F0F9FF;
            color: var(--train-blue);
            box-shadow: 0 4px 12px rgba(2, 132, 199, 0.18);
        }

        .mode-tab-btn.active.mode-theater {
            border-color: var(--cinema-purple);
            background: #FAF5FF;
            color: var(--cinema-purple);
            box-shadow: 0 4px 12px rgba(124, 58, 237, 0.18);
        }

        .mode-pill-tag {
            font-size: 10px;
            font-weight: 800;
            padding: 2px 7px;
            border-radius: var(--radius-full);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .mode-doorstep .mode-pill-tag { background: #FFE4E6; color: var(--tomato-red); }
        .mode-train .mode-pill-tag { background: #E0F2FE; color: var(--train-blue); }
        .mode-theater .mode-pill-tag { background: #F3E8FF; color: var(--cinema-purple); }

        /* Dynamic Delivery Input Box */
        .mode-details-card {
            margin-top: 12px;
            background: #F8FAFC;
            border: 1.5px solid #E2E8F0;
            border-radius: var(--radius-md);
            padding: 14px 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            flex-wrap: wrap;
        }

        .mode-details-card.train-active {
            border-color: #BAE6FD;
            background: linear-gradient(135deg, #F0F9FF 0%, #FFFFFF 100%);
        }

        .mode-details-card.theater-active {
            border-color: #E9D5FF;
            background: linear-gradient(135deg, #FAF5FF 0%, #FFFFFF 100%);
        }

        .mode-fields-row {
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
            flex: 1;
        }

        .mode-field-item {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .mode-field-item label {
            font-size: 11px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: #64748B;
        }

        .mode-field-item select, .mode-field-item input {
            padding: 7px 12px;
            border-radius: var(--radius-sm);
            border: 1px solid #CBD5E1;
            background: white;
            font-size: 13px;
            font-weight: 700;
            color: var(--charcoal);
            outline: none;
        }

        .mode-field-item select:focus, .mode-field-item input:focus {
            border-color: var(--tomato-red);
            box-shadow: 0 0 0 2px var(--tomato-glow);
        }

        .mode-save-btn {
            background: var(--charcoal);
            color: white;
            padding: 9px 18px;
            border-radius: var(--radius-sm);
            font-weight: 800;
            font-size: 13px;
            display: flex;
            align-items: center;
            gap: 6px;
            align-self: flex-end;
        }
        .mode-save-btn:hover {
            background: black;
        }

        /* ---------------- HERO BANNER ---------------- */
        .hero-banner {
            background: linear-gradient(135deg, #E23744 0%, #C82333 60%, #9B111E 100%);
            color: white;
            padding: 40px 20px;
            position: relative;
            overflow: hidden;
        }

        .hero-banner::before {
            content: "🍅";
            position: absolute;
            right: 4%;
            top: -20px;
            font-size: 240px;
            opacity: 0.1;
            pointer-events: none;
            transform: rotate(15deg);
        }

        .hero-container {
            max-width: 1260px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 30px;
            position: relative;
            z-index: 2;
        }

        .hero-content h1 {
            font-size: clamp(26px, 3.8vw, 42px);
            font-weight: 800;
            line-height: 1.15;
            margin-bottom: 10px;
        }

        .hero-content p {
            font-size: 15.5px;
            opacity: 0.94;
            max-width: 640px;
            margin-bottom: 20px;
            line-height: 1.5;
        }

        .hero-badges {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }

        .hero-badge-item {
            background: rgba(255, 255, 255, 0.18);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 6px 14px;
            border-radius: var(--radius-full);
            font-size: 12.5px;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .hero-interactive-card {
            background: white;
            color: var(--text-main);
            padding: 18px 22px;
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-lg);
            min-width: 310px;
            border: 2px solid #FFE4E6;
        }

        .hero-courier-row {
            display: flex;
            align-items: center;
            gap: 14px;
            margin-bottom: 12px;
        }

        .hero-courier-avatar {
            font-size: 42px;
            background: #FFF1F2;
            width: 62px;
            height: 62px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 2px dashed var(--tomato-red);
            flex-shrink: 0;
        }

        .hero-courier-meta h4 {
            font-size: 16px;
            font-weight: 800;
            color: var(--charcoal);
        }

        .hero-courier-meta p {
            font-size: 12px;
            color: var(--text-muted);
        }

        .hero-spin-banner-btn {
            width: 100%;
            background: var(--gold-gradient);
            color: #000;
            padding: 10px;
            border-radius: var(--radius-md);
            font-weight: 800;
            font-size: 13.5px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            box-shadow: 0 4px 14px rgba(245, 158, 11, 0.4);
        }
        .hero-spin-banner-btn:hover {
            transform: translateY(-2px);
        }

        /* ---------------- SECTION CONTAINER ---------------- */
        .section-container {
            max-width: 1260px;
            margin: 32px auto 0;
            padding: 0 20px;
        }

        .section-title {
            display: flex;
            align-items: baseline;
            gap: 12px;
            margin-bottom: 18px;
        }

        .section-title h3 {
            font-size: 24px;
            font-weight: 800;
            color: var(--charcoal);
            letter-spacing: -0.5px;
        }

        .section-title span.sub-count {
            color: var(--text-muted);
            font-size: 14px;
            font-weight: 600;
        }

        /* ---------------- CUISINES SCROLL ROW ---------------- */
        .cuisine-row-scroll {
            display: flex;
            gap: 20px;
            overflow-x: auto;
            padding: 10px 4px 20px;
            scrollbar-width: thin;
        }

        .cuisine-row-scroll::-webkit-scrollbar {
            height: 6px;
        }

        .cuisine-row-scroll::-webkit-scrollbar-thumb {
            background: #E5E7EB;
            border-radius: 10px;
        }

        .cuisine-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;
            cursor: pointer;
            flex-shrink: 0;
            width: 90px;
            text-align: center;
            transition: transform 0.2s;
        }

        .cuisine-item:hover {
            transform: translateY(-4px);
        }

        .cuisine-item.active .cuisine-img-wrap {
            box-shadow: 0 0 0 3px var(--tomato-red), 0 6px 14px rgba(226, 55, 68, 0.3);
            transform: scale(1.06);
        }

        .cuisine-item.active .cuisine-name {
            color: var(--tomato-red);
            font-weight: 800;
        }

        .cuisine-img-wrap {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            overflow: hidden;
            background: #FFF;
            box-shadow: var(--shadow-sm);
            border: 2px solid #FFF;
            transition: all 0.2s;
        }

        .cuisine-img-wrap img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .cuisine-name {
            font-size: 13px;
            font-weight: 700;
            color: var(--text-main);
        }

        /* ---------------- FILTER BAR ---------------- */
        .filter-bar {
            display: flex;
            align-items: center;
            gap: 10px;
            overflow-x: auto;
            padding: 8px 0 20px;
            margin-bottom: 10px;
            scrollbar-width: none;
        }

        .filter-bar::-webkit-scrollbar {
            display: none;
        }

        .filter-pill {
            background: white;
            border: 1px solid #E5E7EB;
            padding: 8px 16px;
            border-radius: var(--radius-full);
            font-size: 13.5px;
            font-weight: 600;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 8px;
            white-space: nowrap;
            box-shadow: 0 1px 4px rgba(0, 0, 0, 0.03);
            transition: all 0.15s;
        }

        .filter-pill:hover {
            border-color: #CBD5E1;
            background: #F8FAFC;
        }

        .filter-pill.active {
            background: var(--charcoal);
            color: white;
            border-color: var(--charcoal);
        }

        .filter-pill.veg-active {
            background: var(--veg-light);
            color: var(--veg-green);
            border-color: var(--veg-green);
            font-weight: 800;
        }

        .filter-pill.nonveg-active {
            background: var(--nonveg-light);
            color: var(--nonveg-red);
            border-color: var(--nonveg-red);
            font-weight: 800;
        }

        .veg-symbol {
            display: inline-block;
            width: 13px;
            height: 13px;
            border: 1.5px solid var(--veg-green);
            border-radius: 3px;
            position: relative;
        }
        .veg-symbol::after {
            content: '';
            position: absolute;
            width: 7px;
            height: 7px;
            background: var(--veg-green);
            border-radius: 50%;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }

        .nonveg-symbol {
            display: inline-block;
            width: 13px;
            height: 13px;
            border: 1.5px solid var(--nonveg-red);
            border-radius: 3px;
            position: relative;
        }
        .nonveg-symbol::after {
            content: '';
            position: absolute;
            width: 0;
            height: 0;
            border-left: 4px solid transparent;
            border-right: 4px solid transparent;
            border-bottom: 7px solid var(--nonveg-red);
            top: 50%;
            left: 50%;
            transform: translate(-50%, -55%);
        }

        /* ---------------- RESTAURANTS GRID ---------------- */
        .restaurants-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(310px, 1fr));
            gap: 26px;
            margin-bottom: 40px;
        }

        .restaurant-card {
            background: white;
            border-radius: var(--radius-lg);
            overflow: hidden;
            border: 1px solid #ECECEC;
            box-shadow: var(--shadow-sm);
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            cursor: pointer;
            display: flex;
            flex-direction: column;
            position: relative;
        }

        .restaurant-card:hover {
            transform: translateY(-6px);
            box-shadow: var(--shadow-lg);
            border-color: #DFDFDF;
        }

        .card-banner {
            position: relative;
            width: 100%;
            height: 190px;
            overflow: hidden;
            background: #E5E7EB;
        }

        .card-banner img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.4s ease;
        }

        .restaurant-card:hover .card-banner img {
            transform: scale(1.05);
        }

        .card-offer-badge {
            position: absolute;
            bottom: 12px;
            left: 12px;
            background: rgba(28, 28, 28, 0.88);
            backdrop-filter: blur(6px);
            color: #FFD700;
            font-weight: 800;
            font-size: 11.5px;
            padding: 4px 10px;
            border-radius: 6px;
            letter-spacing: 0.3px;
        }

        .card-veg-type {
            position: absolute;
            top: 12px;
            left: 12px;
            background: white;
            padding: 4px 8px;
            border-radius: var(--radius-sm);
            font-size: 11px;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 5px;
            box-shadow: var(--shadow-sm);
        }

        .card-fav-btn {
            position: absolute;
            top: 12px;
            right: 12px;
            width: 34px;
            height: 34px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(4px);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
            box-shadow: var(--shadow-sm);
            transition: transform 0.15s;
        }
        .card-fav-btn:hover {
            transform: scale(1.15);
        }

        .card-body {
            padding: 16px 18px;
            display: flex;
            flex-direction: column;
            flex: 1;
        }

        .card-header-row {
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 8px;
            margin-bottom: 6px;
        }

        .restaurant-name {
            font-size: 17px;
            font-weight: 800;
            color: var(--charcoal);
            line-height: 1.25;
        }

        .rating-badge {
            background: #24963F;
            color: white;
            font-size: 12px;
            font-weight: 800;
            padding: 3px 7px;
            border-radius: 6px;
            display: flex;
            align-items: center;
            gap: 3px;
            flex-shrink: 0;
        }

        .card-cuisines {
            font-size: 13px;
            color: var(--text-muted);
            margin-bottom: 12px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .card-meta-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-top: 1px solid #F1F1F1;
            padding-top: 12px;
            margin-top: auto;
            font-size: 12.5px;
            color: #4B5563;
            font-weight: 600;
        }

        /* ---------------- FLOATING SPIN & WIN BUTTON ---------------- */
        .floating-spin-btn {
            position: fixed;
            bottom: 24px;
            right: 24px;
            z-index: 99;
            background: linear-gradient(135deg, #FF416C 0%, #FF4B2B 100%);
            color: white;
            padding: 12px 20px;
            border-radius: var(--radius-full);
            box-shadow: 0 8px 24px rgba(255, 75, 43, 0.45);
            font-weight: 800;
            font-size: 14px;
            display: flex;
            align-items: center;
            gap: 8px;
            cursor: pointer;
            transition: all 0.25s;
            animation: pulseFloating 2.5s infinite;
        }

        .floating-spin-btn:hover {
            transform: scale(1.08) rotate(-1deg);
            box-shadow: 0 12px 30px rgba(255, 75, 43, 0.6);
        }

        @keyframes pulseFloating {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.04); }
        }

        .floating-badge {
            background: #FFD700;
            color: #000;
            font-size: 10px;
            font-weight: 900;
            padding: 2px 6px;
            border-radius: var(--radius-full);
            text-transform: uppercase;
        }

        /* ---------------- GAMES & SPIN WHEEL MODAL ---------------- */
        .games-modal-backdrop {
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.85);
            backdrop-filter: blur(10px);
            z-index: 250;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 16px;
        }

        .games-modal-backdrop.open {
            display: flex;
        }

        .games-hub-box {
            background: #18181B;
            color: white;
            border-radius: var(--radius-lg);
            width: 100%;
            max-width: 680px;
            max-height: 90vh;
            overflow-y: auto;
            position: relative;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
            border: 2px solid #3F3F46;
            display: flex;
            flex-direction: column;
        }

        .games-hub-header {
            padding: 18px 24px;
            border-bottom: 1px solid #27272A;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .games-hub-header h3 {
            font-size: 20px;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 8px;
            color: #FFD700;
        }

        .games-close-btn {
            background: #27272A;
            color: #A1A1AA;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            font-size: 16px;
            font-weight: 800;
        }
        .games-close-btn:hover {
            color: white;
            background: #3F3F46;
        }

        /* Game Switcher Tabs */
        .games-nav-tabs {
            display: flex;
            border-bottom: 1px solid #27272A;
            background: #121215;
        }

        .game-tab-btn {
            flex: 1;
            padding: 12px;
            font-size: 13.5px;
            font-weight: 800;
            color: #A1A1AA;
            background: transparent;
            border-bottom: 3px solid transparent;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
        }

        .game-tab-btn.active {
            color: #FFD700;
            border-bottom-color: #FFD700;
            background: rgba(255, 215, 0, 0.05);
        }

        .game-panel-body {
            padding: 24px;
            display: none;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }

        .game-panel-body.active {
            display: flex;
        }

        /* Spin the Wheel UI */
        .wheel-outer-wrap {
            position: relative;
            width: 340px;
            height: 340px;
            margin: 12px auto 20px;
        }

        #wheelCanvas {
            width: 340px;
            height: 340px;
            border-radius: 50%;
            box-shadow: 0 0 35px rgba(245, 158, 11, 0.45);
            transition: transform 4s cubic-bezier(0.17, 0.67, 0.12, 0.99);
        }

        .wheel-pointer {
            position: absolute;
            top: -12px;
            left: 50%;
            transform: translateX(-50%);
            width: 0;
            height: 0;
            border-left: 18px solid transparent;
            border-right: 18px solid transparent;
            border-top: 30px solid #FFD700;
            filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.4));
            z-index: 10;
        }

        .wheel-center-cap {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: #18181B;
            border: 4px solid #FFD700;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 26px;
            box-shadow: 0 0 16px rgba(0, 0, 0, 0.7);
            z-index: 8;
        }

        .spin-action-btn {
            background: var(--gold-gradient);
            color: #000;
            padding: 12px 36px;
            border-radius: var(--radius-full);
            font-size: 16px;
            font-weight: 800;
            box-shadow: 0 6px 20px rgba(245, 158, 11, 0.5);
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .spin-action-btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
        }
        .spin-action-btn:hover:not(:disabled) {
            transform: scale(1.05);
        }

        /* Wheel Prize Reveal Alert */
        .wheel-prize-alert {
            margin-top: 16px;
            background: #27272A;
            border: 2px dashed #FFD700;
            border-radius: var(--radius-md);
            padding: 16px 20px;
            width: 100%;
            display: none;
            flex-direction: column;
            align-items: center;
            gap: 8px;
            animation: fadeIn 0.3s ease;
        }

        .prize-rare-tag {
            background: #DC2626;
            color: white;
            font-size: 11px;
            font-weight: 900;
            padding: 2px 8px;
            border-radius: var(--radius-full);
            text-transform: uppercase;
        }

        .prize-won-code {
            background: #000;
            color: #FFD700;
            font-family: monospace;
            font-size: 18px;
            font-weight: 800;
            padding: 6px 16px;
            border-radius: var(--radius-sm);
            border: 1px solid #FFD700;
            letter-spacing: 2px;
        }

        .apply-wheel-code-btn {
            background: #10B981;
            color: white;
            padding: 8px 20px;
            border-radius: var(--radius-sm);
            font-weight: 800;
            font-size: 13px;
        }

        /* Arcade Mini-Game Canvas */
        #arcadeCanvas {
            background: #09090B;
            border: 2px solid #27272A;
            border-radius: var(--radius-md);
            width: 340px;
            height: 240px;
            margin: 10px 0;
            box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.8);
        }

        .arcade-controls-row {
            display: flex;
            gap: 12px;
            margin-top: 8px;
        }

        .arcade-btn {
            background: #27272A;
            color: white;
            padding: 10px 24px;
            border-radius: var(--radius-sm);
            font-weight: 800;
            font-size: 15px;
        }
        .arcade-btn:active {
            background: #3F3F46;
        }

        /* ---------------- RESTAURANT MENU MODAL ---------------- */
        .modal-backdrop {
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.75);
            backdrop-filter: blur(8px);
            z-index: 200;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 16px;
        }

        .modal-backdrop.open {
            display: flex;
        }

        .restaurant-modal {
            background: white;
            border-radius: var(--radius-lg);
            width: 100%;
            max-width: 780px;
            max-height: 90vh;
            overflow-y: auto;
            position: relative;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.25);
            display: flex;
            flex-direction: column;
        }

        .modal-close-btn {
            position: absolute;
            top: 14px;
            right: 14px;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background: rgba(0, 0, 0, 0.65);
            color: white;
            font-size: 18px;
            z-index: 10;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .modal-header-hero {
            position: relative;
            height: 200px;
            background: #111;
        }

        .modal-header-hero img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            opacity: 0.85;
        }

        .modal-header-info {
            position: absolute;
            bottom: 16px;
            left: 20px;
            right: 20px;
            color: white;
            text-shadow: 0 2px 6px rgba(0, 0, 0, 0.6);
        }

        .modal-header-info h2 {
            font-size: 24px;
            font-weight: 800;
        }

        .modal-delivery-meta-bar {
            background: #F8FAFC;
            border-bottom: 1px solid #E2E8F0;
            padding: 12px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 13px;
            font-weight: 700;
            color: #475569;
        }

        .menu-modal-body {
            padding: 20px;
            overflow-y: auto;
        }

        .menu-dish-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 16px;
            padding: 16px 0;
            border-bottom: 1px solid #F1F1F1;
        }

        .dish-info {
            flex: 1;
        }

        .dish-top-meta {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 4px;
        }

        .dish-name {
            font-size: 15px;
            font-weight: 800;
            color: var(--charcoal);
        }

        .dish-price {
            font-size: 14px;
            font-weight: 700;
            color: #374151;
            margin-bottom: 4px;
        }

        .dish-desc {
            font-size: 12.5px;
            color: var(--text-muted);
            line-height: 1.4;
            max-width: 440px;
        }

        .dish-action-side {
            display: flex;
            flex-direction: column;
            align-items: center;
            position: relative;
            width: 100px;
        }

        .dish-img-thumb {
            width: 90px;
            height: 90px;
            border-radius: var(--radius-md);
            object-fit: cover;
            border: 1px solid #ECECEC;
        }

        .dish-add-btn {
            background: white;
            color: var(--tomato-red);
            border: 1.5px solid var(--tomato-red);
            padding: 6px 18px;
            border-radius: var(--radius-sm);
            font-size: 13px;
            font-weight: 800;
            box-shadow: var(--shadow-sm);
            margin-top: -16px;
            z-index: 2;
        }
        .dish-add-btn:hover {
            background: #FFF5F5;
        }

        .dish-qty-stepper {
            display: flex;
            align-items: center;
            background: var(--tomato-red);
            color: white;
            border-radius: var(--radius-sm);
            overflow: hidden;
            margin-top: -16px;
            z-index: 2;
            box-shadow: var(--shadow-sm);
        }

        .dish-qty-stepper button {
            background: transparent;
            color: white;
            padding: 4px 10px;
            font-size: 14px;
            font-weight: 800;
        }

        .dish-qty-stepper span {
            padding: 2px 8px;
            font-size: 12px;
            font-weight: 800;
        }

        /* ---------------- CART DRAWER ---------------- */
        .cart-drawer-backdrop {
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(4px);
            z-index: 210;
            display: none;
        }

        .cart-drawer-backdrop.open {
            display: block;
        }

        .cart-drawer {
            position: fixed;
            top: 0;
            right: -460px;
            width: 100%;
            max-width: 440px;
            height: 100vh;
            background: white;
            z-index: 220;
            box-shadow: -6px 0 30px rgba(0, 0, 0, 0.18);
            transition: right 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            display: flex;
            flex-direction: column;
        }

        .cart-drawer.open {
            right: 0;
        }

        .drawer-header {
            padding: 16px 20px;
            border-bottom: 1px solid #ECECEC;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .drawer-header h3 {
            font-size: 18px;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .drawer-body {
            padding: 20px;
            overflow-y: auto;
            flex: 1;
        }

        .drawer-footer {
            padding: 16px 20px;
            border-top: 1px solid #ECECEC;
            background: #FAFAFA;
        }

        .checkout-btn {
            width: 100%;
            background: var(--tomato-red);
            color: white;
            padding: 14px;
            border-radius: var(--radius-md);
            font-size: 15px;
            font-weight: 800;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 4px 16px rgba(226, 55, 68, 0.35);
        }
        .checkout-btn:hover {
            background: var(--tomato-dark);
        }

        .cart-item-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 14px;
        }

        .cart-item-name {
            font-size: 13.5px;
            font-weight: 700;
            color: var(--charcoal);
        }

        .cart-target-destination-card {
            background: #F0F9FF;
            border: 1.5px solid #BAE6FD;
            border-radius: var(--radius-md);
            padding: 12px 14px;
            margin-bottom: 16px;
            font-size: 12.5px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .cart-target-destination-card.mode-theater-card {
            background: #FAF5FF;
            border-color: #E9D5FF;
        }

        .cart-target-destination-card.mode-doorstep-card {
            background: #FFF5F5;
            border-color: #FECDD3;
        }

        .coupon-box {
            display: flex;
            gap: 8px;
            margin: 16px 0;
        }

        .coupon-box input {
            flex: 1;
            padding: 9px 12px;
            border: 1px dashed #CBD5E1;
            border-radius: var(--radius-sm);
            font-size: 13px;
            font-weight: 700;
            text-transform: uppercase;
        }

        .coupon-apply-btn {
            background: var(--charcoal);
            color: white;
            padding: 8px 16px;
            border-radius: var(--radius-sm);
            font-weight: 800;
            font-size: 12.5px;
        }

        .bill-section {
            background: #F8FAFC;
            border-radius: var(--radius-md);
            padding: 14px 16px;
            font-size: 13px;
            border: 1px solid #E2E8F0;
        }

        .bill-line {
            display: flex;
            justify-content: space-between;
            margin-bottom: 8px;
            color: #64748B;
        }

        .bill-line.total {
            border-top: 1px dashed #CBD5E1;
            padding-top: 8px;
            margin-top: 8px;
            font-size: 15px;
            font-weight: 800;
            color: var(--charcoal);
        }

        .payment-notice-card {
            background: #FFFBEB;
            border: 1.5px solid #FDE68A;
            border-radius: var(--radius-md);
            padding: 12px 14px;
            margin-top: 16px;
            font-size: 12.5px;
            color: #92400E;
        }

        /* ---------------- PRANK / SCREAMING GOAT MODAL ---------------- */
        .prank-modal-wrap {
            position: fixed;
            inset: 0;
            background: rgba(10, 10, 10, 0.94);
            backdrop-filter: blur(12px);
            z-index: 300;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 16px;
        }

        .prank-modal-wrap.open {
            display: flex;
        }

        .screen-shake {
            animation: crazyShake 0.4s infinite;
        }

        @keyframes crazyShake {
            0% { transform: translate(0, 0) rotate(0deg); }
            20% { transform: translate(-8px, 6px) rotate(-1.5deg); }
            40% { transform: translate(8px, -6px) rotate(1.5deg); }
            60% { transform: translate(-6px, -4px) rotate(-1deg); }
            80% { transform: translate(6px, 4px) rotate(1deg); }
            100% { transform: translate(0, 0) rotate(0deg); }
        }

        .siren-flash {
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 310;
            display: none;
            background: radial-gradient(circle, rgba(226, 55, 68, 0.45) 0%, rgba(245, 158, 11, 0.55) 100%);
        }

        .siren-flash.active {
            display: block;
            animation: sirenBlink 0.15s infinite alternate;
        }

        @keyframes sirenBlink {
            from { opacity: 0.2; }
            to { opacity: 0.85; }
        }

        .prank-loader-card {
            background: #18181B;
            border: 2px solid #3F3F46;
            border-radius: var(--radius-lg);
            padding: 40px;
            text-align: center;
            color: white;
            max-width: 440px;
            width: 100%;
        }

        .spinning-tomato {
            font-size: 64px;
            display: inline-block;
            animation: spinFast 0.8s linear infinite;
            margin-bottom: 20px;
        }

        @keyframes spinFast {
            0% { transform: rotate(0deg) scale(1); }
            50% { transform: rotate(180deg) scale(1.15); }
            100% { transform: rotate(360deg) scale(1); }
        }

        /* The Meme Reveal Card with Multiple Cartoon & Real Goat Memes */
        .meme-reveal-card {
            background: #111;
            border: 3px solid var(--tomato-red);
            border-radius: var(--radius-lg);
            width: 100%;
            max-width: 580px;
            overflow: hidden;
            display: none;
            flex-direction: column;
            align-items: center;
            text-align: center;
            box-shadow: 0 0 50px rgba(226, 55, 68, 0.6);
            animation: memePop 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            max-height: 94vh;
            overflow-y: auto;
        }

        @keyframes memePop {
            0% { transform: scale(0.3); opacity: 0; }
            100% { transform: scale(1); opacity: 1; }
        }

        .meme-impact-header {
            background: var(--tomato-red);
            color: white;
            font-family: 'Outfit', sans-serif;
            font-size: clamp(18px, 4vw, 24px);
            font-weight: 900;
            width: 100%;
            padding: 12px 16px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        /* Meme Selector Tabs (Cartoon Billy, Chef Billy, Real Goat) */
        .meme-tabs-switcher {
            display: flex;
            width: 100%;
            background: #1F1F23;
            border-bottom: 1px solid #333;
        }

        .meme-tab-btn {
            flex: 1;
            padding: 10px;
            font-size: 12px;
            font-weight: 800;
            color: #BBB;
            background: transparent;
            border-bottom: 3px solid transparent;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 5px;
        }

        .meme-tab-btn.active {
            color: #FFD700;
            border-bottom-color: #FFD700;
            background: rgba(255, 215, 0, 0.08);
        }

        .meme-stage-media {
            width: 100%;
            height: 310px;
            position: relative;
            background: #000;
            overflow: hidden;
            cursor: pointer;
        }

        .real-goat-photo {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        .meme-impact-footer {
            background: #000;
            color: #FFD700;
            font-family: 'Outfit', sans-serif;
            font-size: clamp(15px, 3.2vw, 20px);
            font-weight: 900;
            width: 100%;
            padding: 10px 16px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            border-top: 1px solid #222;
        }

        /* Soundboard Bar */
        .billy-soundboard-bar {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            justify-content: center;
            padding: 10px 16px;
            background: #1C1C1E;
            width: 100%;
            border-bottom: 1px solid #2C2C2E;
        }

        .soundboard-chip-btn {
            background: #2C2C2E;
            color: #FFF;
            padding: 6px 12px;
            border-radius: var(--radius-full);
            font-size: 12px;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 5px;
            border: 1px solid #3A3A3C;
        }
        .soundboard-chip-btn:hover {
            background: #E23744;
            border-color: #E23744;
            transform: scale(1.05);
        }

        .billy-fun-comment-box {
            background: #18181B;
            border: 1px dashed #F59E0B;
            border-radius: var(--radius-md);
            margin: 12px 16px;
            padding: 12px 16px;
            display: flex;
            align-items: center;
            gap: 12px;
            text-align: left;
        }

        .billy-fun-comment-box .goat-chat-avatar {
            font-size: 32px;
            flex-shrink: 0;
        }

        .meme-prank-disclaimer {
            padding: 14px 20px 20px;
            width: 100%;
        }

        .meme-buttons-row {
            display: flex;
            gap: 12px;
            justify-content: center;
            margin-top: 16px;
            flex-wrap: wrap;
        }

        .replay-goat-btn {
            background: #EF4444;
            color: white;
            padding: 10px 20px;
            border-radius: var(--radius-full);
            font-weight: 800;
            font-size: 13.5px;
        }

        .track-real-order-btn {
            background: #10B981;
            color: white;
            padding: 10px 22px;
            border-radius: var(--radius-full);
            font-weight: 800;
            font-size: 13.5px;
        }

        /* ---------------- LIVE TRACKER CARD ---------------- */
        .live-tracker-card {
            background: white;
            border-radius: var(--radius-lg);
            width: 100%;
            max-width: 540px;
            overflow: hidden;
            display: none;
            flex-direction: column;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
            max-height: 90vh;
            overflow-y: auto;
        }

        .tracker-header {
            background: var(--charcoal);
            color: white;
            padding: 18px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .simulated-map {
            position: relative;
            width: 100%;
            height: 170px;
            background: #E2E8F0;
            overflow: hidden;
        }

        .map-road {
            position: absolute;
            top: 50%;
            left: 0;
            right: 0;
            height: 18px;
            background: #64748B;
            transform: translateY(-50%);
        }

        .map-goat-courier {
            position: absolute;
            top: 50%;
            left: 10%;
            transform: translateY(-50%);
            font-size: 38px;
            animation: goatDrive 8s linear infinite;
        }

        @keyframes goatDrive {
            0% { left: 5%; transform: translateY(-50%) scaleX(1); }
            48% { left: 80%; transform: translateY(-50%) scaleX(1); }
            50% { transform: translateY(-50%) scaleX(-1); }
            98% { left: 5%; transform: translateY(-50%) scaleX(-1); }
            100% { transform: translateY(-50%) scaleX(1); }
        }

        .map-target-pin {
            position: absolute;
            top: 50%;
            right: 12%;
            transform: translateY(-50%);
            font-size: 32px;
        }

        .tracker-body {
            padding: 20px;
        }

        .tracker-courier-box {
            display: flex;
            align-items: center;
            gap: 14px;
            background: #FFF8F8;
            border: 1.5px solid #FFD6D9;
            border-radius: var(--radius-md);
            padding: 12px 16px;
            margin-bottom: 16px;
        }

        .tracker-courier-box .courier-avatar {
            font-size: 36px;
            background: white;
            width: 52px;
            height: 52px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 2px solid var(--tomato-red);
        }

        /* ---------------- FOOTER ---------------- */
        footer {
            background: #111;
            color: #A0A0A0;
            padding: 50px 20px 30px;
            border-top: 1px solid #252525;
            margin-top: 50px;
        }

        .footer-inner {
            max-width: 1260px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 2fr 1fr 1fr 1fr;
            gap: 30px;
            padding-bottom: 30px;
            border-bottom: 1px solid #252525;
        }

        .footer-brand h3 {
            font-size: 26px;
            font-weight: 800;
            color: white;
            margin-bottom: 8px;
        }

        .footer-col h4 {
            font-size: 14px;
            font-weight: 700;
            color: white;
            margin-bottom: 14px;
            text-transform: uppercase;
        }

        .footer-col ul {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 8px;
            font-size: 13px;
        }

        .footer-bottom {
            max-width: 1260px;
            margin: 20px auto 0;
            text-align: center;
            font-size: 12.5px;
            color: #666;
        }

        @media (max-width: 860px) {
            .header-inner { flex-wrap: wrap; }
            .search-locality-wrap { order: 3; width: 100%; min-width: 100%; }
            .hero-container { flex-direction: column; align-items: flex-start; }
            .footer-inner { grid-template-columns: 1fr 1fr; }
        }

        @media (max-width: 600px) {
            .footer-inner { grid-template-columns: 1fr; }
            .restaurants-grid { grid-template-columns: 1fr; }
            .mode-tabs-bar { width: 100%; }
        }
    </style>
</head>

<body>

    <!-- Real Goat Sound Audio Element -->
    <audio id="goatAudio" src="goat_scream.wav" preload="auto"></audio>

    <!-- Siren Flash on Prank -->
    <div class="siren-flash" id="sirenFlash"></div>

    <!-- ---------------- TOP ANNOUNCEMENT / ARCADE STRIP ---------------- -->
    <div class="scratch-announcement-strip">
        <span class="scratch-strip-badge">🎡 TOMATO ARCADE</span>
        <span>Spin the Lucky Wheel or Catch Samosas to win <strong>100% OFF</strong> & <strong>Rare Golden Prizes!</strong></span>
        <button class="scratch-strip-cta" onclick="openGamesHub('wheel')">
            <span>🎡</span> Spin Wheel Now
        </button>
        <button class="scratch-strip-cta" style="background:#FFD700; color:#000;" onclick="openGamesHub('arcade')">
            <span>🎮</span> Mini-Game
        </button>
    </div>

    <!-- ---------------- HEADER ---------------- -->
    <header class="top-header">
        <div class="header-inner">
            <div class="logo-box" onclick="resetFilters()">
                🍅 Tomato <span class="logo-sub">DELIVERIES & CHAOS</span>
            </div>

            <div class="search-locality-wrap">
                <div class="locality-selector" onclick="focusLocalityOrMode()">
                    <span id="headerLocIcon">📍</span>
                    <select id="localitySelect" onchange="onLocalityChange()">
                        <option value="Koramangala, Bangalore">Koramangala, BLR</option>
                        <option value="Indiranagar, Bangalore">Indiranagar, BLR</option>
                        <option value="HSR Layout, Bangalore">HSR Layout, BLR</option>
                        <option value="Connaught Place, New Delhi">Connaught Place, DEL</option>
                        <option value="Cyber Hub, Gurgaon">Cyber Hub, GGN</option>
                        <option value="Bandra West, Mumbai">Bandra West, BOM</option>
                        <option value="Powai, Mumbai">Powai, BOM</option>
                        <option value="Jubilee Hills, Hyderabad">Jubilee Hills, HYD</option>
                        <option value="Anna Nagar, Chennai">Anna Nagar, MAA</option>
                        <option value="Salt Lake, Kolkata">Salt Lake, CCU</option>
                    </select>
                </div>

                <div class="search-input-box">
                    <span>🔍</span>
                    <input type="text" id="searchInput" placeholder="Search for Butter Chicken, Sundaes, Samosas, Biryani..." oninput="handleSearch()">
                </div>
            </div>

            <div class="header-actions">
                <button class="games-header-btn" onclick="openGamesHub('wheel')">
                    <span>🎡</span> Spin & Win
                </button>
                <div class="mode-header-badge" id="modeHeaderBadge" onclick="scrollToDeliveryMode()">
                    <span>🛵</span> Doorstep Mode
                </div>
                <button class="cart-btn-main" onclick="openCartDrawer()">
                    <span>🛒</span> Cart
                    <span class="cart-badge-count" id="cartCountBadge">0</span>
                </button>
            </div>
        </div>
    </header>

    <!-- ---------------- DELIVERY MODE SELECTOR (TRAIN / THEATER / DOORSTEP) ---------------- -->
    <section class="delivery-modes-strip" id="deliveryModeSection">
        <div class="delivery-modes-container">
            <div class="mode-tabs-bar">
                <button class="mode-tab-btn active mode-doorstep" id="tabDoorstep" onclick="switchDeliveryMode('doorstep')">
                    <span>🛵</span> Standard Doorstep
                    <span class="mode-pill-tag">Home / Office</span>
                </button>
                <button class="mode-tab-btn mode-train" id="tabTrain" onclick="switchDeliveryMode('train')">
                    <span>🚆</span> Deliver to Train Coach & Berth
                    <span class="mode-pill-tag">IRCTC Express</span>
                </button>
                <button class="mode-tab-btn mode-theater" id="tabTheater" onclick="switchDeliveryMode('theater')">
                    <span>🎬</span> Deliver to Cinema Seat
                    <span class="mode-pill-tag">Interval Express</span>
                </button>
            </div>

            <!-- Dynamic Mode Form Details -->
            <div class="mode-details-card" id="modeDetailsCard">
                <!-- Injected via switchDeliveryMode JS -->
            </div>
        </div>
    </section>

    <!-- ---------------- HERO BANNER ---------------- -->
    <section class="hero-banner">
        <div class="hero-container">
            <div class="hero-content">
                <h1 id="heroHeadline">Delivering Hot Food to Your Door, Train Berth & Cinema Seat! 🍅</h1>
                <p id="heroSubline">Craving Biryani on the train? Popcorn & gourmet burgers at the movie interval? Or late-night ice creams at home? Tomato delivers directly to your seat and door with lightning speed. <strong>Cash on Delivery Only!</strong></p>
                <div class="hero-badges">
                    <span class="hero-badge-item">🚆 Train Seat & Berth Delivery</span>
                    <span class="hero-badge-item">🍿 Cinema Intermission Delivery</span>
                    <span class="hero-badge-item">🍨 Ice Creams & Desserts</span>
                    <span class="hero-badge-item">🍟 Hot Snacks & Chaats</span>
                    <span class="hero-badge-item">💵 Cash on Delivery ONLY</span>
                    <span class="hero-badge-item">🐐 100% Goat Approved</span>
                </div>
            </div>

            <div class="hero-interactive-card">
                <div class="hero-courier-row">
                    <div class="hero-courier-avatar" id="heroAgentAvatar">🐐</div>
                    <div class="hero-courier-meta">
                        <h4 id="heroAgentName">Billy "The GOAT"</h4>
                        <p id="heroAgentLoc">Assigned Partner: On Duty</p>
                        <div style="font-size:11px; color:#10B981; font-weight:800; display:flex; align-items:center; gap:4px; margin-top:2px;">
                            <span>●</span> Ready for Rapid Delivery • 4.9 ★
                        </div>
                    </div>
                </div>
                <button class="hero-spin-banner-btn" onclick="openGamesHub('wheel')">
                    <span>🎡</span> Spin Lucky Wheel for 100% OFF!
                </button>
            </div>
        </div>
    </section>

    <!-- ---------------- INSPIRATION / CUISINE ROW ---------------- -->
    <section class="section-container">
        <div class="section-title">
            <h3>Inspiration for your cravings</h3>
            <span class="sub-count" id="cuisineHeaderCount">12 Categories</span>
        </div>
        <div class="cuisine-row-scroll" id="cuisineList">
            <!-- Injected via JS -->
        </div>

        <!-- Filter Bar -->
        <div class="filter-bar" id="filterBar">
            <button class="filter-pill active" id="filterAll" onclick="setFilter('all')">All Places</button>
            <button class="filter-pill" id="filterVeg" onclick="setFilter('veg')"><span class="veg-symbol"></span> Pure Veg</button>
            <button class="filter-pill" id="filterNonVeg" onclick="setFilter('nonveg')"><span class="nonveg-symbol"></span> Veg & Non-Veg</button>
            <button class="filter-pill" id="filterIceCream" onclick="setFilter('icecream')">🍨 Ice Creams</button>
            <button class="filter-pill" id="filterSnacks" onclick="setFilter('snacks')">🍟 Snacks & Chaats</button>
            <button class="filter-pill" id="filterDesserts" onclick="setFilter('desserts')">🍰 Desserts & Waffles</button>
            <button class="filter-pill" id="filterRating" onclick="setFilter('rating')">⭐ Top Rated 4.5+</button>
            <button class="filter-pill" id="filterFast" onclick="setFilter('fast')">⚡ Fast Delivery (<25m)</button>
            <button class="filter-pill" id="filterOffer" onclick="setFilter('offer')">🏷️ Great Offers</button>
        </div>
    </section>

    <!-- ---------------- RESTAURANTS SECTION ---------------- -->
    <section class="section-container">
        <div class="section-title">
            <h3 id="restaurantsHeaderTitle">Food Delivery Restaurants</h3>
            <span class="sub-count" id="placesCount">Loading places...</span>
        </div>

        <div class="restaurants-grid" id="restaurantsGrid">
            <!-- Injected via JS -->
        </div>
    </section>

    <!-- ---------------- FLOATING SPIN & WIN BUTTON ---------------- -->
    <div class="floating-spin-btn" onclick="openGamesHub('wheel')">
        <span>🎡</span>
        <span>Spin & Win</span>
        <span class="floating-badge">Rare Prizes</span>
    </div>

    <!-- ---------------- GAMES & SPIN WHEEL MODAL ---------------- -->
    <div class="games-modal-backdrop" id="gamesModal" onclick="closeGamesOnBackdrop(event)">
        <div class="games-hub-box">
            <div class="games-hub-header">
                <h3><span>🎡</span> Tomato Games & Lucky Deals</h3>
                <button class="games-close-btn" onclick="closeGamesModal()">✕</button>
            </div>

            <div class="games-nav-tabs">
                <button class="game-tab-btn active" id="tabBtnWheel" onclick="switchGameTab('wheel')">
                    <span>🎡</span> Spin The Wheel
                </button>
                <button class="game-tab-btn" id="tabBtnArcade" onclick="switchGameTab('arcade')">
                    <span>🎮</span> Catch Samosas Game
                </button>
                <button class="game-tab-btn" id="tabBtnScratch" onclick="switchGameTab('scratch')">
                    <span>🎁</span> Scratch Cards
                </button>
            </div>

            <!-- Tab 1: Spin The Wheel -->
            <div class="game-panel-body active" id="gamePanelWheel">
                <p style="font-size:13.5px; color:#A1A1AA; max-width:480px; margin-bottom:10px;">
                    Spin the lucky prize wheel to win flat discounts, free sundaes, and the legendary <strong>Golden Goat Trophy</strong> (100% OFF)!
                </p>

                <div class="wheel-outer-wrap">
                    <div class="wheel-pointer"></div>
                    <canvas id="wheelCanvas" width="340" height="340"></canvas>
                    <div class="wheel-center-cap">🍅</div>
                </div>

                <button class="spin-action-btn" id="wheelSpinBtn" onclick="spinWheel()">
                    <span>🎡</span> SPIN THE WHEEL NOW!
                </button>

                <!-- Won Prize Display -->
                <div class="wheel-prize-alert" id="wheelPrizeAlert">
                    <span class="prize-rare-tag" id="prizeRareTag">🎉 PRIZE UNLOCKED!</span>
                    <h4 id="wheelPrizeTitle" style="font-size:18px; color:white;">Golden Goat Trophy</h4>
                    <p id="wheelPrizeDesc" style="font-size:13px; color:#D4D4D8;">100% OFF on your entire Cash-on-Delivery bill!</p>
                    <div class="prize-won-code" id="wheelPrizeCode">GOLDENGOAT</div>
                    <button class="apply-wheel-code-btn" onclick="applyWheelCodeToCart()">
                        📋 Apply Coupon to Cart & Shop!
                    </button>
                </div>
            </div>

            <!-- Tab 2: Mini Arcade Game (Catch Samosas & Pizzas) -->
            <div class="game-panel-body" id="gamePanelArcade">
                <p style="font-size:13.5px; color:#A1A1AA; max-width:480px; margin-bottom:8px;">
                    Move Billy left & right to catch falling pizzas, samosas, and ice creams! Dodge alarm clocks. Score 40+ to unlock secret <strong>60% OFF</strong>!
                </p>
                <div style="display:flex; justify-content:space-between; width:340px; font-size:13px; font-weight:800; color:#FFD700; margin-bottom:4px;">
                    <span id="arcadeScore">Score: 0</span>
                    <span id="arcadeTimer">Time: 20s</span>
                </div>
                <canvas id="arcadeCanvas" width="340" height="240"></canvas>
                <div class="arcade-controls-row">
                    <button class="arcade-btn" onmousedown="moveArcadeLeft()" ontouchstart="moveArcadeLeft()">◀ LEFT</button>
                    <button class="arcade-btn" style="background:#10B981;" id="arcadeStartBtn" onclick="startArcadeGame()">▶ START GAME</button>
                    <button class="arcade-btn" onmousedown="moveArcadeRight()" ontouchstart="moveArcadeRight()">RIGHT ▶</button>
                </div>
                <div id="arcadeWinAlert" style="display:none; margin-top:10px; background:#27272A; border:1px solid #10B981; border-radius:8px; padding:10px 16px;">
                    <span style="color:#10B981; font-weight:800;">🎉 Arcade Champion! Unlocked 60% OFF: </span>
                    <span style="font-family:monospace; font-weight:800; color:#FFD700;">ARCADE60</span>
                    <button onclick="applyArcadeCode()" style="margin-left:8px; background:#10B981; color:white; padding:4px 10px; border-radius:4px; font-weight:800; font-size:11px;">Apply</button>
                </div>
            </div>

            <!-- Tab 3: Scratch & Win -->
            <div class="game-panel-body" id="gamePanelScratch">
                <p style="font-size:13.5px; color:#A1A1AA; max-width:480px; margin-bottom:12px;">
                    Scratch with your mouse or finger to uncover mystery discounts up to 70% OFF!
                </p>
                <div style="position:relative; width:300px; height:160px; margin:0 auto 16px; border-radius:12px; overflow:hidden;">
                    <div style="position:absolute; inset:0; background:linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%); display:flex; flex-direction:column; align-items:center; justify-content:center; color:#92400E; padding:12px; border:2px dashed #D97706;">
                        <div style="font-size:32px;" id="scratchIcon">🍨</div>
                        <div style="font-size:16px; font-weight:800;" id="scratchTitle">FLAT 70% OFF COD</div>
                        <div style="font-size:11px;">Valid on all Cash on Delivery orders</div>
                        <div style="background:#000; color:#FFD700; padding:4px 12px; border-radius:4px; font-family:monospace; font-weight:800; font-size:14px; margin-top:4px;" id="scratchCodeTag">GOAT70</div>
                    </div>
                    <canvas id="scratchCanvas" width="300" height="160" style="position:absolute; inset:0; cursor:crosshair;"></canvas>
                </div>
                <div style="display:flex; gap:10px;">
                    <button class="spin-action-btn" style="padding:8px 20px; font-size:14px;" onclick="applyScratchedCode()">📋 Copy & Apply to Cart</button>
                    <button style="background:#3F3F46; color:white; padding:8px 14px; border-radius:var(--radius-full); font-size:12px; font-weight:700;" onclick="revealScratchCard()">✨ Reveal</button>
                </div>
            </div>
        </div>
    </div>

    <!-- ---------------- RESTAURANT MENU MODAL ---------------- -->
    <div class="modal-backdrop" id="restaurantModal" onclick="closeModalOnBackdrop(event)">
        <div class="restaurant-modal" id="restaurantModalContent">
            <button class="modal-close-btn" onclick="closeRestaurantModal()">✕</button>
            <div class="modal-header-hero">
                <img id="modalHeroImg" src="" alt="Restaurant Banner">
                <div class="modal-header-info">
                    <h2 id="modalRestName">Restaurant Name</h2>
                    <p id="modalRestCuisines">North Indian, Mughlai • ₹350 for two</p>
                </div>
            </div>

            <div class="modal-delivery-meta-bar">
                <div id="modalRestStats">⭐ 4.5 • 25-30 mins • 2.1 km</div>
                <div class="modal-agent-indicator">
                    <span id="modalDeliveryIcon">🛵</span> Delivery to: <strong id="modalDeliveryTarget">Doorstep</strong>
                </div>
            </div>

            <div class="menu-modal-body" id="modalMenuBody">
                <!-- Dishes injected via JS -->
            </div>
        </div>
    </div>

    <!-- ---------------- CART DRAWER ---------------- -->
    <div class="cart-drawer-backdrop" id="cartDrawerBackdrop" onclick="closeCartDrawer()"></div>
    <div class="cart-drawer" id="cartDrawer">
        <div class="drawer-header">
            <h3><span>🛒</span> Your Tomato Cart</h3>
            <button onclick="closeCartDrawer()" style="font-size:20px; font-weight:700;">✕</button>
        </div>

        <div class="drawer-body" id="drawerBody">
            <!-- Injected via JS -->
        </div>

        <div class="drawer-footer" id="drawerFooter">
            <!-- Checkout button injected via JS -->
        </div>
    </div>

    <!-- ---------------- PRANK / SCREAMING GOAT REVEAL MODAL ---------------- -->
    <div class="prank-modal-wrap" id="prankModalWrap">

        <!-- Step 1: Realistic Loader -->
        <div class="prank-loader-card" id="prankLoader">
            <div class="spinning-tomato">🍅</div>
            <div class="loader-status-text" id="loaderStatusText" style="font-size:18px; font-weight:800; margin-bottom:8px;">Connecting with Restaurant Kitchen...</div>
            <div class="loader-sub-text" id="loaderSubText" style="font-size:13px; color:#A1A1AA;">Dispatching courier to your exact seat & berth.</div>
        </div>

        <!-- Step 2: The Screaming Goat Viral Meme Card (WITH MULTIPLE CARTOON & REAL GOAT MEMES + SOUNDBOARD) -->
        <div class="meme-reveal-card" id="memeRevealCard">
            <div class="meme-impact-header">HOLD UP! DID YOU THINK</div>

            <!-- Meme Switcher Tabs -->
            <div class="meme-tabs-switcher">
                <button class="meme-tab-btn active" id="memeTab1" onclick="switchMeme('delivery_cartoon')">
                    <span>🛵</span> Cartoon Courier Billy
                </button>
                <button class="meme-tab-btn" id="memeTab2" onclick="switchMeme('chef_cartoon')">
                    <span>👨‍🍳</span> Cartoon Chef Billy
                </button>
                <button class="meme-tab-btn" id="memeTab3" onclick="switchMeme('real_goat')">
                    <span>🐐</span> Real Goat Meme
                </button>
            </div>

            <div class="meme-stage-media" onclick="playRealGoatSound()">
                <img id="activeMemeImg" src="cartoon_goat_delivery.jpg" class="real-goat-photo" alt="Funny Goat Meme">
            </div>

            <div class="meme-impact-footer" id="activeMemeFooter">
                YOU COULD GET FOOD WITHOUT THE GOAT?! 📢 BAAAAAAH!
            </div>

            <!-- Interactive Billy Soundboard -->
            <div class="billy-soundboard-bar">
                <span style="font-size:11px; font-weight:800; color:#A1A1AA; align-self:center;">GOAT SOUNDBOARD:</span>
                <button class="soundboard-chip-btn" onclick="playRealGoatSound()">
                    <span>🔊</span> Real Goat Scream
                </button>
                <button class="soundboard-chip-btn" onclick="playCartoonBleat()">
                    <span>📢</span> Cartoon Bleat
                </button>
                <button class="soundboard-chip-btn" onclick="playGoatLaugh()">
                    <span>🤣</span> Goat Laugh
                </button>
                <button class="soundboard-chip-btn" onclick="playCrunchSound()">
                    <span>🥕</span> Munch & Crunch
                </button>
            </div>

            <!-- Billy's Dynamic Delivery Comment Box -->
            <div class="billy-fun-comment-box">
                <div class="goat-chat-avatar">🐐</div>
                <div>
                    <strong style="color:#FFB800; font-size:12.5px; display:block; margin-bottom:2px;" id="billyCommentTitle">Billy Courier says:</strong>
                    <p id="billyRandomFunComment" style="font-size:13px; color:#E5E7EB; line-height:1.4;">"I personally inspected your order on the highway and sampled 2 bites of the snack. Quality passed! 10/10 service. BAAAAAAH!"</p>
                </div>
            </div>

            <div class="meme-prank-disclaimer">
                <p style="font-size:13px; color:#E5E7EB; line-height:1.4;">
                    💥 <strong>SIKE! YOU JUST GOT GOATED!</strong> Tomato is 100% fun, but your hunger is 100% real.
                    Your Cash-on-Delivery order is actually placed!
                </p>

                <div class="meme-buttons-row">
                    <button class="replay-goat-btn" onclick="playRealGoatSound()">
                        <span>🔊</span> Hear Real Scream!
                    </button>
                    <button class="track-real-order-btn" onclick="showLiveTracker()">
                        <span>🛵</span> Track My Delivery 😂
                    </button>
                </div>
            </div>
        </div>

        <!-- Step 3: Live Goat Delivery Tracker (Adapts to Train / Theater / Doorstep) -->
        <div class="live-tracker-card" id="liveTrackerCard">
            <div class="tracker-header">
                <div>
                    <h3 id="trackerTitleText">Order Confirmed! 🎉</h3>
                    <span style="font-size:12px; opacity:0.8;">Payment: Cash on Delivery</span>
                </div>
                <span class="order-badge" id="trackerOrderId" style="background:#E23744; padding:4px 10px; border-radius:6px; font-weight:800; font-size:12px;">#TOM-82910</span>
            </div>

            <div class="simulated-map">
                <div class="map-road"></div>
                <div class="map-goat-courier" id="mapCourierIcon">🐐💨</div>
                <div class="map-target-pin" id="mapTargetPin">📍🏠</div>
                <div style="position:absolute; bottom:10px; left:12px; background:rgba(0,0,0,0.75); color:white; padding:4px 12px; border-radius:999px; font-size:11.5px; font-weight:700;" id="mapStatusPill">Status: Trotting along highway at 42 km/h</div>
            </div>

            <div class="tracker-body">
                <div class="tracker-courier-box">
                    <div class="courier-avatar" id="trackerCourierAvatar">🐐</div>
                    <div class="courier-info">
                        <h4 id="trackerAgentName">Billy "The Screaming Goat"</h4>
                        <p id="trackerVehicleMeta">Vehicle: Turbo Goat Scooter • 4.9 ★</p>
                    </div>
                    <div style="margin-left:auto; display:flex; gap:6px;">
                        <button onclick="playCrunchSound()" style="background:#EA580C; color:white; padding:6px 10px; border-radius:6px; font-size:11.5px; font-weight:700;">🥕 Feed</button>
                        <button onclick="playRealGoatSound()" style="background:#10B981; color:white; padding:6px 10px; border-radius:6px; font-size:11.5px; font-weight:700;">📞 Call</button>
                    </div>
                </div>

                <div id="trackerDeliveryTargetInfo" style="background:#F1F5F9; border:1px solid #CBD5E1; border-radius:8px; padding:10px 14px; margin-bottom:14px; font-size:12.5px; font-weight:700;">
                    📍 Delivering to: Koramangala, Bangalore
                </div>

                <div style="background:#FEF3C7; border-left:4px solid #F59E0B; padding:10px 14px; border-radius:4px; font-size:12.5px; color:#92400E; margin-bottom:16px;" id="trackerFunnyQuote">
                    💬 "Billy's note: Please keep exact cash ready. My hooves cannot hold loose change."
                </div>

                <button onclick="closePrankAndReset()" style="width:100%; background:var(--charcoal); color:white; padding:12px; border-radius:var(--radius-md); font-weight:800; font-size:14px;">
                    Order Again / Back to Home 🍅
                </button>
            </div>
        </div>
    </div>

    <!-- ---------------- FOOTER ---------------- -->
    <footer>
        <div class="footer-inner">
            <div class="footer-brand">
                <h3>🍅 Tomato</h3>
                <p>The ultimate parody food delivery app inspired by Zomato. We deliver delicious food, hot samosas, desserts, and ice creams directly to your doorstep, train coach berth, or movie theater seat. Only Cash on Delivery accepted!</p>
            </div>
            <div class="footer-col">
                <h4>Delivery Services</h4>
                <ul>
                    <li><a href="javascript:void(0)" onclick="switchDeliveryMode('doorstep')">Doorstep Delivery</a></li>
                    <li><a href="javascript:void(0)" onclick="switchDeliveryMode('train')">Train Seat & Berth Delivery</a></li>
                    <li><a href="javascript:void(0)" onclick="switchDeliveryMode('theater')">Cinema Hall Delivery</a></li>
                    <li><a href="javascript:void(0)" onclick="openGamesHub('wheel')">Spin The Wheel Discounts</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Popular Cuisines</h4>
                <ul>
                    <li><a href="javascript:void(0)" onclick="selectCuisine('biryani')">Biryani & Kebabs</a></li>
                    <li><a href="javascript:void(0)" onclick="selectCuisine('icecream')">Artisan Ice Creams</a></li>
                    <li><a href="javascript:void(0)" onclick="selectCuisine('snacks')">Chaat & Samosas</a></li>
                    <li><a href="javascript:void(0)" onclick="selectCuisine('desserts')">Waffles & Desserts</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Help & Legal</h4>
                <ul>
                    <li><a href="javascript:void(0)">Cash on Delivery FAQ</a></li>
                    <li><a href="javascript:void(0)">Goat Safety Policy</a></li>
                    <li><a href="javascript:void(0)">IRCTC Food Guidelines</a></li>
                    <li><a href="javascript:void(0)">Cinema Delivery FAQ</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>© 2026 Tomato Delivery Ltd. A playful parody tribute to Zomato. All screaming goats are trained professionals.</p>
        </div>
    </footer>

    <!-- =================================================================
         APPLICATION JAVASCRIPT LOGIC
         ================================================================= -->
    <script>
        /* ==========================================================
           1. COMPREHENSIVE DATA: RESTAURANTS, CUISINES, PRIZES
           ========================================================== */
        const CUISINES = [
            { id: 'all', name: 'All', img: 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=200&auto=format&fit=crop&q=80' },
            { id: 'icecream', name: 'Ice Creams', img: 'https://images.unsplash.com/photo-1497034825429-c343d7c6a68f?w=200&auto=format&fit=crop&q=80' },
            { id: 'desserts', name: 'Desserts', img: 'https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=200&auto=format&fit=crop&q=80' },
            { id: 'snacks', name: 'Snacks & Chaat', img: 'https://images.unsplash.com/photo-1601050690597-df0568f70950?w=200&auto=format&fit=crop&q=80' },
            { id: 'biryani', name: 'Biryani', img: 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=200&auto=format&fit=crop&q=80' },
            { id: 'pizza', name: 'Pizzas', img: 'https://images.unsplash.com/photo-1513104890138-7c749659a591?w=200&auto=format&fit=crop&q=80' },
            { id: 'burger', name: 'Burgers', img: 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=200&auto=format&fit=crop&q=80' },
            { id: 'north_indian', name: 'North Indian', img: 'https://images.unsplash.com/photo-1589302168068-964664d93dc0?w=200&auto=format&fit=crop&q=80' },
            { id: 'chinese', name: 'Chinese', img: 'https://images.unsplash.com/photo-1585032226651-759b368d7246?w=200&auto=format&fit=crop&q=80' },
            { id: 'south_indian', name: 'South Indian', img: 'https://images.unsplash.com/photo-1610192244261-3f33de3f55e4?w=200&auto=format&fit=crop&q=80' },
            { id: 'rolls', name: 'Rolls & Wraps', img: 'https://images.unsplash.com/photo-1626777552726-4a6b54c97e46?w=200&auto=format&fit=crop&q=80' },
            { id: 'shakes', name: 'Thick Shakes', img: 'https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=200&auto=format&fit=crop&q=80' }
        ];

        const RESTAURANTS = [
            {
                id: 'rest-1',
                name: 'Polar Bear Ice Cream Sundaes',
                cuisineId: 'icecream',
                cuisineTags: ['Ice Creams', 'Desserts', 'Sundaes'],
                rating: 4.8,
                time: '18 mins',
                costForTwo: '₹250 for two',
                locality: 'Koramangala, Bangalore',
                pureVeg: true,
                offer: 'FLAT 50% OFF up to ₹100',
                img: 'https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=600&auto=format&fit=crop&q=80',
                menu: [
                    { id: 'd-101', name: 'Death By Chocolate Sundae', price: 219, veg: true, desc: 'Rich chocolate cake, layered vanilla ice cream, hot chocolate fudge, cherries, and toasted nuts.', img: 'https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=300&auto=format&fit=crop&q=80' },
                    { id: 'd-102', name: 'Gudbud Royal Sundae', price: 199, veg: true, desc: 'Famous tri-flavor sundae with fresh mango, strawberry, dry fruits, and jelly.', img: 'https://images.unsplash.com/photo-1501443762994-82bd5dace89a?w=300&auto=format&fit=crop&q=80' },
                    { id: 'd-103', name: 'Nutty Belgian Dark Chocolate Tub (500ml)', price: 289, veg: true, desc: 'Velvety 70% dark Belgian cocoa ice cream studded with roasted hazelnuts.', img: 'https://images.unsplash.com/photo-1570197788417-0e82375c9371?w=300&auto=format&fit=crop&q=80' }
                ]
            },
            {
                id: 'rest-2',
                name: 'The Belgian Waffle Co.',
                cuisineId: 'desserts',
                cuisineTags: ['Desserts', 'Waffles', 'Pancakes'],
                rating: 4.7,
                time: '20 mins',
                costForTwo: '₹300 for two',
                locality: 'Indiranagar, Bangalore',
                pureVeg: true,
                offer: 'Buy 1 Get 1 Free',
                img: 'https://images.unsplash.com/photo-1562376552-0d160a2f238d?w=600&auto=format&fit=crop&q=80',
                menu: [
                    { id: 'd-201', name: 'Nutella Overload Waff-wich', price: 185, veg: true, desc: 'Freshly baked warm crispy waffle loaded with copious Nutella and chocolate pearls.', img: 'https://images.unsplash.com/photo-1562376552-0d160a2f238d?w=300&auto=format&fit=crop&q=80' },
                    { id: 'd-202', name: 'Triple Chocolate Mini Pancakes (12 Pcs)', price: 175, veg: true, desc: 'Fluffy bite-sized pancakes drenched in white, milk, and dark Belgian chocolate.', img: 'https://images.unsplash.com/photo-1528198691077-705f9634f4cd?w=300&auto=format&fit=crop&q=80' }
                ]
            },
            {
                id: 'rest-3',
                name: 'Haldirams & Chai Point Street Snacks',
                cuisineId: 'snacks',
                cuisineTags: ['Snacks & Chaat', 'Street Food', 'North Indian'],
                rating: 4.6,
                time: '15 mins',
                costForTwo: '₹200 for two',
                locality: 'Connaught Place, New Delhi',
                pureVeg: true,
                offer: '60% OFF up to ₹120',
                img: 'https://images.unsplash.com/photo-1601050690597-df0568f70950?w=600&auto=format&fit=crop&q=80',
                menu: [
                    { id: 'd-301', name: 'Delhi Special Samosa Platter (4 Pcs)', price: 110, veg: true, desc: 'Crispy flaky crust stuffed with spicy cumin potatoes, served with mint & tamarind chutney.', img: 'https://images.unsplash.com/photo-1601050690597-df0568f70950?w=300&auto=format&fit=crop&q=80' },
                    { id: 'd-302', name: 'Dahi Papdi Chaat Supreme', price: 140, veg: true, desc: 'Crispy papdis topped with spiced potatoes, chilled sweet curd, sev, and pomegranate seeds.', img: 'https://images.unsplash.com/photo-1589301760014-d929f3979dbc?w=300&auto=format&fit=crop&q=80' },
                    { id: 'd-303', name: 'Paneer Bread Pakoda Combo', price: 125, veg: true, desc: 'Stuffed bread pakoda with thick cottage cheese slab and piping hot cutting chai.', img: 'https://images.unsplash.com/photo-1599488615731-7e5c2823ff28?w=300&auto=format&fit=crop&q=80' }
                ]
            },
            {
                id: 'rest-4',
                name: 'Behrouz Royal Biryani',
                cuisineId: 'biryani',
                cuisineTags: ['Biryani', 'Mughlai', 'North Indian'],
                rating: 4.9,
                time: '25 mins',
                costForTwo: '₹600 for two',
                locality: 'Koramangala, Bangalore',
                pureVeg: false,
                offer: 'FLAT ₹150 OFF with COD',
                img: 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=600&auto=format&fit=crop&q=80',
                menu: [
                    { id: 'd-401', name: 'Dum Gosht Mutton Biryani', price: 449, veg: false, desc: 'Tender mutton slow-cooked in aromatic aged basmati rice with royal saffron and kewra essence.', img: 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=300&auto=format&fit=crop&q=80' },
                    { id: 'd-402', name: 'Zaikedaar Paneer Biryani', price: 349, veg: true, desc: 'Marinated paneer cubes layered with saffron rice, caramelized onions, and fresh mint.', img: 'https://images.unsplash.com/photo-1633945274405-b6c8069047b0?w=300&auto=format&fit=crop&q=80' }
                ]
            },
            {
                id: 'rest-5',
                name: 'Tossin Woodfired Gourmet Pizza',
                cuisineId: 'pizza',
                cuisineTags: ['Pizzas', 'Italian', 'Snacks'],
                rating: 4.7,
                time: '24 mins',
                costForTwo: '₹550 for two',
                locality: 'Cyber Hub, Gurgaon',
                pureVeg: false,
                offer: 'Buy 1 Get 1 Large Pizza',
                img: 'https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600&auto=format&fit=crop&q=80',
                menu: [
                    { id: 'd-501', name: 'Peri-Peri Smoked Chicken Pizza', price: 420, veg: false, desc: 'Spicy peri-peri chicken, roasted red peppers, jalapeños, and fresh mozzarella on thin crust.', img: 'https://images.unsplash.com/photo-1513104890138-7c749659a591?w=300&auto=format&fit=crop&q=80' },
                    { id: 'd-502', name: 'Truffle & Burrata Margherita', price: 380, veg: true, desc: 'San Marzano tomato base, artisanal creamy burrata, fresh basil, and white truffle oil drizzle.', img: 'https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=300&auto=format&fit=crop&q=80' }
                ]
            },
            {
                id: 'rest-6',
                name: 'Keventers Thick Shakes & Churros',
                cuisineId: 'desserts',
                cuisineTags: ['Desserts', 'Thick Shakes', 'Ice Creams'],
                rating: 4.6,
                time: '18 mins',
                costForTwo: '₹280 for two',
                locality: 'Bandra West, Mumbai',
                pureVeg: true,
                offer: 'Flat 40% OFF',
                img: 'https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=600&auto=format&fit=crop&q=80',
                menu: [
                    { id: 'd-601', name: 'Belgian Chocolate Thickshake', price: 189, veg: true, desc: 'Thick creamy heritage milkshake with rich cocoa nibs in iconic glass bottle.', img: 'https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=300&auto=format&fit=crop&q=80' },
                    { id: 'd-602', name: 'Cinnamon Sugar Spanish Churros (6 Pcs)', price: 169, veg: true, desc: 'Golden crispy churros dusted with cinnamon sugar, served with warm chocolate dip.', img: 'https://images.unsplash.com/photo-1624300629298-e9de39c13be5?w=300&auto=format&fit=crop&q=80' }
                ]
            }
        ];

        /* Wheel Prizes (Discounts & Rare Prizes) */
        const WHEEL_SECTORS = [
            { label: '🏆 GOLDEN GOAT', code: 'GOLDENGOAT', desc: '100% OFF up to ₹500 (Rare Prize!)', color: '#D97706', isRare: true },
            { label: '🍕 50% OFF', code: 'SPIN50', desc: 'Flat 50% OFF on entire food order!', color: '#EF4444', isRare: false },
            { label: '🎟️ VIP PASS', code: 'GOATVIP', desc: 'Free Delivery + ₹200 OFF (Rare Prize!)', color: '#8B5CF6', isRare: true },
            { label: '🍨 FREE SUNDAE', code: 'FREESUNDAE', desc: 'Flat ₹150 OFF on Ice Creams & Desserts', color: '#EC4899', isRare: false },
            { label: '🎁 MYSTERY BOX', code: 'MYSTERYBOX', desc: 'Flat ₹100 OFF + Free Surprise Snack!', color: '#F59E0B', isRare: false },
            { label: '🥟 FREE SAMOSAS', code: 'SAMOSAWIN', desc: 'Flat ₹80 OFF on Street Snacks', color: '#10B981', isRare: false },
            { label: '💥 ₹120 CASH', code: 'CASH120', desc: 'Flat ₹120 Instant Cashback on COD', color: '#3B82F6', isRare: false },
            { label: '🐐 BLESSINGS', code: 'BLESS25', desc: '25% OFF + Billy The Goat Blessings', color: '#6366F1', isRare: false }
        ];

        /* Delivery Destinations State */
        let deliveryMode = 'doorstep'; // 'doorstep' | 'train' | 'theater'
        let trainDetails = {
            trainNo: '12952 - Mumbai - New Delhi Rajdhani Express',
            station: 'Bhopal Junction (BPL)',
            coach: 'Coach B3 (3rd AC)',
            berth: 'Berth 42 (Lower)',
            pnr: '2458910423'
        };
        let theaterDetails = {
            multiplex: "PVR Director's Cut - Ambience Mall",
            audi: "Audi 3 (Dolby Atmos)",
            seat: "Row H, Seat 14"
        };
        let currentLocality = "Koramangala, Bangalore";

        /* Cart & App State */
        let cart = {};
        let appliedCoupon = null;
        let currentFilter = 'all';
        let currentCuisine = 'all';
        let searchQuery = '';
        let audioCtx = null;
        let isWheelSpinning = false;
        let currentWheelAngle = 0;

        /* Arcade Game State */
        let arcadeInterval = null;
        let arcadeTimerInterval = null;
        let arcadeScore = 0;
        let arcadeTimeLeft = 20;
        let arcadePlayerX = 140;
        let arcadeItems = [];

        /* ==========================================================
           2. DELIVERY MODE SWITCHING (TRAIN / THEATER / DOORSTEP)
           ========================================================== */
        function switchDeliveryMode(mode) {
            deliveryMode = mode;

            document.getElementById('tabDoorstep').classList.toggle('active', mode === 'doorstep');
            document.getElementById('tabTrain').classList.toggle('active', mode === 'train');
            document.getElementById('tabTheater').classList.toggle('active', mode === 'theater');

            const card = document.getElementById('modeDetailsCard');
            const badge = document.getElementById('modeHeaderBadge');
            const locIcon = document.getElementById('headerLocIcon');
            const heroHead = document.getElementById('heroHeadline');

            if (mode === 'doorstep') {
                badge.innerHTML = `<span>🛵</span> Doorstep Mode`;
                locIcon.textContent = `📍`;
                heroHead.textContent = `Tomato 🍅 — Delivering Real Food to Your Doorstep!`;
                card.className = `mode-details-card`;
                card.innerHTML = `
                    <div class="mode-fields-row">
                        <div class="mode-field-item">
                            <label>Delivery Destination</label>
                            <span style="font-size:14px; font-weight:800; color:var(--tomato-red);">🛵 Standard Home / Office Delivery</span>
                        </div>
                        <div class="mode-field-item">
                            <label>Locality</label>
                            <span style="font-size:13.5px; font-weight:700;">${currentLocality}</span>
                        </div>
                    </div>
                    <div style="font-size:12px; color:#64748B;">⚡ Guaranteed 18–30 min delivery by our locality fleet. Cash on Delivery only.</div>
                `;
            } else if (mode === 'train') {
                badge.innerHTML = `<span>🚆</span> Train #${trainDetails.trainNo.split(' ')[0]} • ${trainDetails.coach}, ${trainDetails.berth}`;
                locIcon.textContent = `🚆`;
                heroHead.textContent = `Hot Food Delivered Right to Your Train Berth! 🚆`;
                card.className = `mode-details-card train-active`;
                card.innerHTML = `
                    <div class="mode-fields-row">
                        <div class="mode-field-item">
                            <label>Train Number / Name</label>
                            <select id="trainNoSelect" onchange="updateTrainFields()">
                                <option value="12952 - New Delhi Rajdhani" selected>12952 - New Delhi Rajdhani</option>
                                <option value="12626 - Kerala Express">12626 - Kerala Express</option>
                                <option value="12002 - Bhopal Shatabdi">12002 - Bhopal Shatabdi</option>
                                <option value="12296 - Sanghamitra Express">12296 - Sanghamitra Express</option>
                                <option value="12138 - Punjab Mail">12138 - Punjab Mail</option>
                            </select>
                        </div>
                        <div class="mode-field-item">
                            <label>Upcoming Station Stop</label>
                            <select id="trainStationSelect" onchange="updateTrainFields()">
                                <option value="Bhopal Junction (BPL)" selected>Bhopal Junction (BPL)</option>
                                <option value="New Delhi (NDLS)">New Delhi (NDLS)</option>
                                <option value="Surat (ST)">Surat (ST)</option>
                                <option value="Vadodara (BRC)">Vadodara (BRC)</option>
                                <option value="Nagpur Junction (NGP)">Nagpur Junction (NGP)</option>
                                <option value="Itarsi Junction (ET)">Itarsi Junction (ET)</option>
                            </select>
                        </div>
                        <div class="mode-field-item">
                            <label>Coach (e.g. B3, A1)</label>
                            <input type="text" id="trainCoachInput" value="${trainDetails.coach}" placeholder="e.g. B3" style="width:110px;" onchange="updateTrainFields()">
                        </div>
                        <div class="mode-field-item">
                            <label>Berth / Seat No.</label>
                            <input type="text" id="trainBerthInput" value="${trainDetails.berth}" placeholder="e.g. Berth 42" style="width:130px;" onchange="updateTrainFields()">
                        </div>
                    </div>
                    <button class="mode-save-btn" onclick="saveTrainSeat()">
                        <span>✓</span> Set Train Seat
                    </button>
                `;
            } else if (mode === 'theater') {
                badge.innerHTML = `<span>🎬</span> ${theaterDetails.multiplex.split(' - ')[0]} • ${theaterDetails.audi}, ${theaterDetails.seat}`;
                locIcon.textContent = `🍿`;
                heroHead.textContent = `Gourmet Food Delivered to Your Cinema Seat! 🍿🎬`;
                card.className = `mode-details-card theater-active`;
                card.innerHTML = `
                    <div class="mode-fields-row">
                        <div class="mode-field-item">
                            <label>Cinema / Multiplex</label>
                            <select id="theaterNameSelect" onchange="updateTheaterFields()">
                                <option value="PVR Director's Cut - Ambience Mall" selected>PVR Director's Cut - Ambience Mall</option>
                                <option value="INOX Megaplex - Phoenix Marketcity">INOX Megaplex - Phoenix Marketcity</option>
                                <option value="Cinepolis VIP - Orion Mall">Cinepolis VIP - Orion Mall</option>
                                <option value="PVR INOX Gold Class - Palladium">PVR INOX Gold Class - Palladium</option>
                            </select>
                        </div>
                        <div class="mode-field-item">
                            <label>Screen / Audi Number</label>
                            <select id="theaterAudiSelect" onchange="updateTheaterFields()">
                                <option value="Audi 3 (Dolby Atmos)" selected>Audi 3 (Dolby Atmos)</option>
                                <option value="Audi 1 (IMAX Laser)">Audi 1 (IMAX Laser)</option>
                                <option value="Audi 4 (4DX Motion)">Audi 4 (4DX Motion)</option>
                                <option value="Audi 2 (VIP Recliners)">Audi 2 (VIP Recliners)</option>
                            </select>
                        </div>
                        <div class="mode-field-item">
                            <label>Row & Seat Number</label>
                            <input type="text" id="theaterSeatInput" value="${theaterDetails.seat}" placeholder="e.g. Row H, Seat 14" style="width:160px;" onchange="updateTheaterFields()">
                        </div>
                    </div>
                    <button class="mode-save-btn" style="background:var(--cinema-purple);" onclick="saveTheaterSeat()">
                        <span>✓</span> Set Cinema Seat
                    </button>
                `;
            }

            updateCourierPill();
            updateCartUI();
        }

        function updateTrainFields() {
            const no = document.getElementById('trainNoSelect')?.value || trainDetails.trainNo;
            const st = document.getElementById('trainStationSelect')?.value || trainDetails.station;
            const co = document.getElementById('trainCoachInput')?.value || trainDetails.coach;
            const be = document.getElementById('trainBerthInput')?.value || trainDetails.berth;
            trainDetails = { trainNo: no, station: st, coach: co, berth: be, pnr: '2458910423' };
        }

        function saveTrainSeat() {
            updateTrainFields();
            alert(`🚆 Train Seat Saved!\nTrain: ${trainDetails.trainNo}\nStation: ${trainDetails.station}\nSeat: ${trainDetails.coach}, ${trainDetails.berth}\nHot food will be delivered directly to your berth! 🍅`);
            switchDeliveryMode('train');
        }

        function updateTheaterFields() {
            const mul = document.getElementById('theaterNameSelect')?.value || theaterDetails.multiplex;
            const aud = document.getElementById('theaterAudiSelect')?.value || theaterDetails.audi;
            const sea = document.getElementById('theaterSeatInput')?.value || theaterDetails.seat;
            theaterDetails = { multiplex: mul, audi: aud, seat: sea };
        }

        function saveTheaterSeat() {
            updateTheaterFields();
            alert(`🎬 Cinema Seat Saved!\nTheater: ${theaterDetails.multiplex}\nScreen: ${theaterDetails.audi}\nSeat: ${theaterDetails.seat}\nHot food will be delivered to your seat during intermission! 🍿`);
            switchDeliveryMode('theater');
        }

        function scrollToDeliveryMode() {
            document.getElementById('deliveryModeSection').scrollIntoView({ behavior: 'smooth' });
        }

        function focusLocalityOrMode() {
            scrollToDeliveryMode();
        }

        function updateCourierPill() {
            const avatar = document.getElementById('heroAgentAvatar');
            const name = document.getElementById('heroAgentName');
            const loc = document.getElementById('heroAgentLoc');

            if (deliveryMode === 'train') {
                avatar.textContent = `🚆`;
                name.textContent = `Birju (Platform Runner)`;
                loc.textContent = `Assigned to: ${trainDetails.station}`;
            } else if (deliveryMode === 'theater') {
                avatar.textContent = `🍿`;
                name.textContent = `Bunty (Cinema Usher)`;
                loc.textContent = `Assigned to: ${theaterDetails.multiplex.split(' - ')[0]}`;
            } else {
                avatar.textContent = `🐐`;
                name.textContent = `Billy "The GOAT"`;
                loc.textContent = `Assigned to: ${currentLocality}`;
            }
        }

        /* ==========================================================
           3. GAMES & LUCKY WHEEL IMPLEMENTATION
           ========================================================== */
        function openGamesHub(tab = 'wheel') {
            document.getElementById('gamesModal').classList.add('open');
            document.body.style.overflow = 'hidden';
            switchGameTab(tab);
            drawWheel();
            initScratchCanvas();
        }

        function closeGamesModal() {
            document.getElementById('gamesModal').classList.remove('open');
            document.body.style.overflow = '';
            stopArcadeGame();
        }

        function closeGamesOnBackdrop(e) {
            if (e.target === document.getElementById('gamesModal')) {
                closeGamesModal();
            }
        }

        function switchGameTab(tab) {
            document.getElementById('tabBtnWheel').classList.toggle('active', tab === 'wheel');
            document.getElementById('tabBtnArcade').classList.toggle('active', tab === 'arcade');
            document.getElementById('tabBtnScratch').classList.toggle('active', tab === 'scratch');

            document.getElementById('gamePanelWheel').classList.toggle('active', tab === 'wheel');
            document.getElementById('gamePanelArcade').classList.toggle('active', tab === 'arcade');
            document.getElementById('gamePanelScratch').classList.toggle('active', tab === 'scratch');

            if (tab === 'wheel') drawWheel();
            if (tab === 'arcade') initArcadeGame();
            if (tab === 'scratch') initScratchCanvas();
        }

        /* Draw Wheel with 8 colorful sectors */
        function drawWheel() {
            const canvas = document.getElementById('wheelCanvas');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            const numSectors = WHEEL_SECTORS.length;
            const arc = (2 * Math.PI) / numSectors;
            const radius = canvas.width / 2;

            ctx.clearRect(0, 0, canvas.width, canvas.height);

            for (let i = 0; i < numSectors; i++) {
                const angle = i * arc;
                ctx.beginPath();
                ctx.fillStyle = WHEEL_SECTORS[i].color;
                ctx.moveTo(radius, radius);
                ctx.arc(radius, radius, radius - 4, angle, angle + arc);
                ctx.lineTo(radius, radius);
                ctx.fill();
                ctx.strokeStyle = '#FFD700';
                ctx.lineWidth = 2.5;
                ctx.stroke();

                // Draw Text
                ctx.save();
                ctx.translate(radius, radius);
                ctx.rotate(angle + arc / 2);
                ctx.textAlign = 'right';
                ctx.fillStyle = '#FFFFFF';
                ctx.font = 'bold 13.5px Outfit, sans-serif';
                ctx.shadowColor = 'rgba(0,0,0,0.8)';
                ctx.shadowBlur = 4;
                ctx.fillText(WHEEL_SECTORS[i].label, radius - 18, 5);
                ctx.restore();
            }
        }

        function spinWheel() {
            if (isWheelSpinning) return;
            isWheelSpinning = true;
            document.getElementById('wheelSpinBtn').disabled = true;
            document.getElementById('wheelPrizeAlert').style.display = 'none';

            // Pick a winning sector (give chance to rare prizes)
            const winningIndex = Math.floor(Math.random() * WHEEL_SECTORS.length);
            const numSectors = WHEEL_SECTORS.length;
            const arcDeg = 360 / numSectors;

            // Compute target degree (Need pointer at top, so 270 deg or subtract from 360)
            const targetSectorAngle = (numSectors - 1 - winningIndex) * arcDeg + (arcDeg / 2);
            const extraSpins = (5 + Math.floor(Math.random() * 3)) * 360;
            const finalAngle = currentWheelAngle + extraSpins + (targetSectorAngle - (currentWheelAngle % 360));
            currentWheelAngle = finalAngle;

            const canvas = document.getElementById('wheelCanvas');
            canvas.style.transform = `rotate(${finalAngle}deg)`;

            // Sound tick interval while spinning
            let tickCounter = 0;
            const tickInterval = setInterval(() => {
                playWheelTick();
                tickCounter++;
                if (tickCounter > 25) clearInterval(tickInterval);
            }, 140);

            setTimeout(() => {
                isWheelSpinning = false;
                document.getElementById('wheelSpinBtn').disabled = false;
                clearInterval(tickInterval);

                const prize = WHEEL_SECTORS[winningIndex];
                revealWheelPrize(prize);
            }, 4100);
        }

        function revealWheelPrize(prize) {
            playFanfare();
            if (typeof confetti === 'function') {
                confetti({ particleCount: 150, spread: 80, origin: { y: 0.6 } });
            }

            const alertBox = document.getElementById('wheelPrizeAlert');
            const rareTag = document.getElementById('prizeRareTag');
            rareTag.style.display = prize.isRare ? 'inline-block' : 'none';
            if (prize.isRare) {
                rareTag.textContent = '🌟 RARE LEGENDARY PRIZE UNLOCKED! 🌟';
            }

            document.getElementById('wheelPrizeTitle').textContent = prize.label;
            document.getElementById('wheelPrizeDesc').textContent = prize.desc;
            document.getElementById('wheelPrizeCode').textContent = prize.code;
            alertBox.style.display = 'flex';
        }

        function applyWheelCodeToCart() {
            const code = document.getElementById('wheelPrizeCode').textContent.trim();
            appliedCoupon = { code: code, discountPct: 0.5, flat: 150 };
            if (code === 'GOLDENGOAT') appliedCoupon = { code: code, discountPct: 1.0, flat: 500 };
            if (code === 'GOATVIP') appliedCoupon = { code: code, discountPct: 0.6, flat: 200 };
            if (code === 'FREESUNDAE') appliedCoupon = { code: code, discountPct: 0.4, flat: 150 };
            if (code === 'MYSTERYBOX') appliedCoupon = { code: code, discountPct: 0.35, flat: 100 };
            if (code === 'SAMOSAWIN') appliedCoupon = { code: code, discountPct: 0.3, flat: 80 };
            if (code === 'CASH120') appliedCoupon = { code: code, discountPct: 0.35, flat: 120 };
            if (code === 'BLESS25') appliedCoupon = { code: code, discountPct: 0.25, flat: 60 };

            updateCartUI();
            closeGamesModal();
            openCartDrawer();
            alert(`🎉 Coupon "${code}" Applied to your cart! Enjoy your discount! 🍅`);
        }

        /* ---------------- ARCADE MINI-GAME (CATCH SAMOSAS & PIZZAS) ---------------- */
        function initArcadeGame() {
            const canvas = document.getElementById('arcadeCanvas');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#111';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = '#FFD700';
            ctx.font = 'bold 15px Outfit, sans-serif';
            ctx.textAlign = 'center';
            ctx.fillText('Press "START GAME" to Play!', 170, 110);
            ctx.font = '12px Plus Jakarta Sans, sans-serif';
            ctx.fillStyle = '#A1A1AA';
            ctx.fillText('Catch 🥟 🍕 🍨 🍔 | Dodge ⏰', 170, 135);
        }

        function startArcadeGame() {
            stopArcadeGame();
            arcadeScore = 0;
            arcadeTimeLeft = 20;
            arcadeItems = [];
            arcadePlayerX = 140;
            document.getElementById('arcadeScore').textContent = `Score: 0`;
            document.getElementById('arcadeTimer').textContent = `Time: 20s`;
            document.getElementById('arcadeWinAlert').style.display = 'none';

            const canvas = document.getElementById('arcadeCanvas');
            const ctx = canvas.getContext('2d');

            arcadeTimerInterval = setInterval(() => {
                arcadeTimeLeft--;
                document.getElementById('arcadeTimer').textContent = `Time: ${arcadeTimeLeft}s`;
                if (arcadeTimeLeft <= 0) {
                    endArcadeGame();
                }
            }, 1000);

            arcadeInterval = setInterval(() => {
                // Spawn new falling item randomly
                if (Math.random() < 0.25) {
                    const isGood = Math.random() > 0.25;
                    const icons = isGood ? ['🥟', '🍕', '🍨', '🍔', '🍅'] : ['⏰', '💣'];
                    arcadeItems.push({
                        x: 20 + Math.random() * 300,
                        y: 0,
                        speed: 3 + Math.random() * 3,
                        icon: icons[Math.floor(Math.random() * icons.length)],
                        isGood: isGood
                    });
                }

                // Update & Render
                ctx.fillStyle = '#09090B';
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                // Draw falling items
                for (let i = arcadeItems.length - 1; i >= 0; i--) {
                    const it = arcadeItems[i];
                    it.y += it.speed;
                    ctx.font = '22px serif';
                    ctx.fillText(it.icon, it.x, it.y);

                    // Check collision with Billy's basket
                    if (it.y >= 200 && it.y <= 235 && Math.abs(it.x - (arcadePlayerX + 25)) < 35) {
                        if (it.isGood) {
                            arcadeScore += 10;
                            playCrunchSound();
                        } else {
                            arcadeScore = Math.max(0, arcadeScore - 10);
                            playCartoonBleat();
                        }
                        document.getElementById('arcadeScore').textContent = `Score: ${arcadeScore}`;
                        arcadeItems.splice(i, 1);
                    } else if (it.y > 240) {
                        arcadeItems.splice(i, 1);
                    }
                }

                // Draw Player (Billy on Scooter / Basket)
                ctx.font = '32px serif';
                ctx.fillText('🐐🛵', arcadePlayerX, 230);

            }, 30);
        }

        function moveArcadeLeft() {
            arcadePlayerX = Math.max(10, arcadePlayerX - 25);
        }

        function moveArcadeRight() {
            arcadePlayerX = Math.min(270, arcadePlayerX + 25);
        }

        window.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowLeft') moveArcadeLeft();
            if (e.key === 'ArrowRight') moveArcadeRight();
        });

        function stopArcadeGame() {
            if (arcadeInterval) clearInterval(arcadeInterval);
            if (arcadeTimerInterval) clearInterval(arcadeTimerInterval);
        }

        function endArcadeGame() {
            stopArcadeGame();
            const canvas = document.getElementById('arcadeCanvas');
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = 'rgba(0,0,0,0.85)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = '#FFD700';
            ctx.font = 'bold 20px Outfit, sans-serif';
            ctx.textAlign = 'center';
            ctx.fillText(`Game Over! Final Score: ${arcadeScore}`, 170, 110);

            if (arcadeScore >= 30) {
                document.getElementById('arcadeWinAlert').style.display = 'block';
                playFanfare();
                if (typeof confetti === 'function') confetti({ particleCount: 80 });
            } else {
                ctx.font = '13px Plus Jakarta Sans, sans-serif';
                ctx.fillStyle = '#FFF';
                ctx.fillText('Score 30+ to unlock secret 60% OFF coupon!', 170, 140);
            }
        }

        function applyArcadeCode() {
            appliedCoupon = { code: 'ARCADE60', discountPct: 0.6, flat: 250 };
            updateCartUI();
            closeGamesModal();
            openCartDrawer();
            alert("🎮 Secret Code ARCADE60 Applied to your cart! 60% OFF unlocked! 🍅");
        }

        /* ---------------- SCRATCH CARD CANVAS ---------------- */
        function initScratchCanvas() {
            const canvas = document.getElementById('scratchCanvas');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            const grad = ctx.createLinearGradient(0, 0, 300, 160);
            grad.addColorStop(0, '#D4AF37');
            grad.addColorStop(0.5, '#FFF2A7');
            grad.addColorStop(1, '#AA771C');
            ctx.fillStyle = grad;
            ctx.fillRect(0, 0, 300, 160);
            ctx.fillStyle = '#1A1102';
            ctx.font = 'bold 14px Plus Jakarta Sans, sans-serif';
            ctx.textAlign = 'center';
            ctx.fillText('✨ RUB TO SCRATCH ✨', 150, 85);

            let isScratching = false;
            function scratchAt(x, y) {
                ctx.globalCompositeOperation = 'destination-out';
                ctx.beginPath();
                ctx.arc(x, y, 20, 0, Math.PI * 2);
                ctx.fill();
            }

            function getCoords(e) {
                const rect = canvas.getBoundingClientRect();
                const cx = e.touches ? e.touches[0].clientX : e.clientX;
                const cy = e.touches ? e.touches[0].clientY : e.clientY;
                return { x: cx - rect.left, y: cy - rect.top };
            }

            canvas.onmousedown = (e) => { isScratching = true; const p = getCoords(e); scratchAt(p.x, p.y); };
            canvas.onmousemove = (e) => { if (isScratching) { const p = getCoords(e); scratchAt(p.x, p.y); } };
            window.onmouseup = () => { isScratching = false; };
            canvas.ontouchstart = (e) => { isScratching = true; const p = getCoords(e); scratchAt(p.x, p.y); };
            canvas.ontouchmove = (e) => { if (isScratching) { const p = getCoords(e); scratchAt(p.x, p.y); } };
            canvas.ontouchend = () => { isScratching = false; };
        }

        function revealScratchCard() {
            const canvas = document.getElementById('scratchCanvas');
            if (canvas) {
                const ctx = canvas.getContext('2d');
                ctx.clearRect(0, 0, canvas.width, canvas.height);
            }
        }

        function applyScratchedCode() {
            appliedCoupon = { code: 'GOAT70', discountPct: 0.7, flat: 300 };
            updateCartUI();
            closeGamesModal();
            openCartDrawer();
            alert("🎁 Scratch Coupon GOAT70 (70% OFF) Applied to your cart! 🍅");
        }

        /* ==========================================================
           4. AUDIO SYNTHESIS & SOUND EFFECTS
           ========================================================== */
        function getAudioContext() {
            if (!audioCtx) {
                const AudioContext = window.AudioContext || window.webkitAudioContext;
                audioCtx = new AudioContext();
            }
            if (audioCtx.state === 'suspended') {
                audioCtx.resume();
            }
            return audioCtx;
        }

        function playRealGoatSound() {
            const audioEl = document.getElementById('goatAudio');
            if (audioEl) {
                audioEl.currentTime = 0;
                audioEl.play().catch(e => {
                    console.log("Audio file blocked, using Web Audio:", e);
                    playWebAudioGoatScream();
                });
            }
            playWebAudioGoatScream();
        }

        function playWebAudioGoatScream() {
            try {
                const ctx = getAudioContext();
                const now = ctx.currentTime;

                const osc1 = ctx.createOscillator();
                osc1.type = 'sawtooth';
                osc1.frequency.setValueAtTime(460, now);
                osc1.frequency.exponentialRampToValueAtTime(780, now + 0.35);
                osc1.frequency.exponentialRampToValueAtTime(320, now + 1.8);

                const osc2 = ctx.createOscillator();
                osc2.type = 'square';
                osc2.frequency.setValueAtTime(455, now);
                osc2.frequency.exponentialRampToValueAtTime(770, now + 0.35);
                osc2.frequency.exponentialRampToValueAtTime(315, now + 1.8);

                const filter = ctx.createBiquadFilter();
                filter.type = 'bandpass';
                filter.frequency.setValueAtTime(1150, now);
                filter.Q.setValueAtTime(3.2, now);

                const gain = ctx.createGain();
                gain.gain.setValueAtTime(0.001, now);
                gain.gain.exponentialRampToValueAtTime(0.7, now + 0.08);
                gain.gain.exponentialRampToValueAtTime(0.001, now + 1.8);

                osc1.connect(filter);
                osc2.connect(filter);
                filter.connect(gain);
                gain.connect(ctx.destination);

                osc1.start(now);
                osc2.start(now);
                osc1.stop(now + 1.85);
                osc2.stop(now + 1.85);
            } catch (err) {
                console.log(err);
            }
        }

        function playCartoonBleat() {
            try {
                const ctx = getAudioContext();
                const now = ctx.currentTime;
                const osc = ctx.createOscillator();
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(600, now);
                osc.frequency.linearRampToValueAtTime(750, now + 0.2);
                osc.frequency.linearRampToValueAtTime(500, now + 0.5);

                const lfo = ctx.createOscillator();
                lfo.frequency.setValueAtTime(18, now);
                const lfoGain = ctx.createGain();
                lfoGain.gain.setValueAtTime(40, now);
                lfo.connect(lfoGain);
                lfoGain.connect(osc.frequency);

                const gain = ctx.createGain();
                gain.gain.setValueAtTime(0.3, now);
                gain.gain.exponentialRampToValueAtTime(0.001, now + 0.5);

                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start(now);
                lfo.start(now);
                osc.stop(now + 0.5);
                lfo.stop(now + 0.5);
            } catch (err) {}
        }

        function playGoatLaugh() {
            try {
                const ctx = getAudioContext();
                const now = ctx.currentTime;
                for (let i = 0; i < 4; i++) {
                    const osc = ctx.createOscillator();
                    osc.type = 'sawtooth';
                    osc.frequency.setValueAtTime(500 + i * 50, now + i * 0.12);
                    osc.frequency.linearRampToValueAtTime(700, now + i * 0.12 + 0.08);

                    const gain = ctx.createGain();
                    gain.gain.setValueAtTime(0.25, now + i * 0.12);
                    gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.12 + 0.1);

                    osc.connect(gain);
                    gain.connect(ctx.destination);
                    osc.start(now + i * 0.12);
                    osc.stop(now + i * 0.12 + 0.11);
                }
            } catch (err) {}
        }

        function playCrunchSound() {
            try {
                const ctx = getAudioContext();
                const now = ctx.currentTime;
                const bufferSize = ctx.sampleRate * 0.15;
                const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
                const data = buffer.getChannelData(0);
                for (let i = 0; i < bufferSize; i++) {
                    data[i] = Math.random() * 2 - 1;
                }
                const noise = ctx.createBufferSource();
                noise.buffer = buffer;
                const filter = ctx.createBiquadFilter();
                filter.type = 'bandpass';
                filter.frequency.setValueAtTime(1400, now);
                const gain = ctx.createGain();
                gain.gain.setValueAtTime(0.4, now);
                gain.gain.exponentialRampToValueAtTime(0.001, now + 0.14);

                noise.connect(filter);
                filter.connect(gain);
                gain.connect(ctx.destination);
                noise.start(now);
            } catch (err) {}
        }

        function playWheelTick() {
            try {
                const ctx = getAudioContext();
                const now = ctx.currentTime;
                const osc = ctx.createOscillator();
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(800, now);
                const gain = ctx.createGain();
                gain.gain.setValueAtTime(0.2, now);
                gain.gain.exponentialRampToValueAtTime(0.001, now + 0.03);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start(now);
                osc.stop(now + 0.035);
            } catch (err) {}
        }

        function playFanfare() {
            try {
                const ctx = getAudioContext();
                const now = ctx.currentTime;
                const notes = [523.25, 659.25, 783.99, 1046.50];
                notes.forEach((freq, idx) => {
                    const osc = ctx.createOscillator();
                    osc.type = 'triangle';
                    osc.frequency.setValueAtTime(freq, now + idx * 0.1);
                    const gain = ctx.createGain();
                    gain.gain.setValueAtTime(0.25, now + idx * 0.1);
                    gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.1 + 0.35);
                    osc.connect(gain);
                    gain.connect(ctx.destination);
                    osc.start(now + idx * 0.1);
                    osc.stop(now + idx * 0.1 + 0.36);
                });
            } catch (err) {}
        }

        /* ==========================================================
           5. RENDERING & FILTERING RESTAURANTS
           ========================================================== */
        function initApp() {
            switchDeliveryMode('doorstep');
            renderCuisines();
            renderRestaurants();
            updateCartUI();
        }

        function renderCuisines() {
            const container = document.getElementById('cuisineList');
            container.innerHTML = CUISINES.map(c => `
                <div class="cuisine-item ${currentCuisine === c.id ? 'active' : ''}" onclick="selectCuisine('${c.id}')">
                    <div class="cuisine-img-wrap">
                        <img src="${c.img}" alt="${c.name}" loading="lazy">
                    </div>
                    <span class="cuisine-name">${c.name}</span>
                </div>
            `).join('');
        }

        function selectCuisine(cuisineId) {
            currentCuisine = (currentCuisine === cuisineId) ? 'all' : cuisineId;
            renderCuisines();
            renderRestaurants();
        }

        function setFilter(type) {
            currentFilter = type;
            document.querySelectorAll('.filter-pill').forEach(b => b.classList.remove('active', 'veg-active', 'nonveg-active'));
            if (type === 'all') document.getElementById('filterAll').classList.add('active');
            if (type === 'veg') document.getElementById('filterVeg').classList.add('veg-active');
            if (type === 'nonveg') document.getElementById('filterNonVeg').classList.add('nonveg-active');
            if (type === 'icecream') document.getElementById('filterIceCream').classList.add('active');
            if (type === 'snacks') document.getElementById('filterSnacks').classList.add('active');
            if (type === 'desserts') document.getElementById('filterDesserts').classList.add('active');
            if (type === 'rating') document.getElementById('filterRating').classList.add('active');
            if (type === 'fast') document.getElementById('filterFast').classList.add('active');
            if (type === 'offer') document.getElementById('filterOffer').classList.add('active');
            renderRestaurants();
        }

        function resetFilters() {
            currentFilter = 'all';
            currentCuisine = 'all';
            searchQuery = '';
            document.getElementById('searchInput').value = '';
            setFilter('all');
            renderCuisines();
            renderRestaurants();
        }

        function handleSearch() {
            searchQuery = document.getElementById('searchInput').value.trim().toLowerCase();
            renderRestaurants();
        }

        function onLocalityChange() {
            currentLocality = document.getElementById('localitySelect').value;
            switchDeliveryMode('doorstep');
            renderRestaurants();
        }

        function renderRestaurants() {
            const grid = document.getElementById('restaurantsGrid');
            const filtered = RESTAURANTS.filter(r => {
                if (currentCuisine !== 'all') {
                    if (r.cuisineId !== currentCuisine && !r.cuisineTags.some(t => t.toLowerCase().includes(currentCuisine))) return false;
                }
                if (currentFilter === 'veg' && !r.pureVeg) return false;
                if (currentFilter === 'nonveg' && r.pureVeg) return false;
                if (currentFilter === 'icecream' && !r.cuisineTags.includes('Ice Creams')) return false;
                if (currentFilter === 'snacks' && !r.cuisineTags.some(t => t.includes('Snack') || t.includes('Street'))) return false;
                if (currentFilter === 'desserts' && !r.cuisineTags.some(t => t.includes('Dessert') || t.includes('Waffle'))) return false;
                if (currentFilter === 'rating' && r.rating < 4.7) return false;
                if (currentFilter === 'fast' && parseInt(r.time) > 20) return false;
                if (currentFilter === 'offer' && !r.offer.includes('50%') && !r.offer.includes('Buy 1')) return false;

                if (searchQuery) {
                    const inName = r.name.toLowerCase().includes(searchQuery);
                    const inCuis = r.cuisineTags.some(c => c.toLowerCase().includes(searchQuery));
                    const inMenu = r.menu.some(m => m.name.toLowerCase().includes(searchQuery));
                    if (!inName && !inCuis && !inMenu) return false;
                }
                return true;
            });

            document.getElementById('placesCount').textContent = `${filtered.length} place${filtered.length === 1 ? '' : 's'} ready for delivery`;

            if (filtered.length === 0) {
                grid.innerHTML = `
                    <div style="grid-column: 1 / -1; text-align: center; padding: 50px 20px; background: white; border-radius: 14px;">
                        <div style="font-size: 48px; margin-bottom: 8px;">🍨</div>
                        <h3>No matching places found</h3>
                        <p style="color: #64748B; margin-bottom: 14px;">Try searching for "Sundae", "Samosa", or "Biryani".</p>
                        <button onclick="resetFilters()" style="background: var(--tomato-red); color: white; padding: 8px 16px; border-radius: 999px; font-weight:700;">Reset Filters</button>
                    </div>
                `;
                return;
            }

            grid.innerHTML = filtered.map(r => `
                <div class="restaurant-card" onclick="openRestaurantModal('${r.id}')">
                    <div class="card-banner">
                        <img src="${r.img}" alt="${r.name}" loading="lazy">
                        <div class="card-offer-badge">${r.offer}</div>
                        <div class="card-veg-type">
                            ${r.pureVeg ? '<span class="veg-symbol"></span> Pure Veg' : '<span class="nonveg-symbol"></span> Veg & Non-Veg'}
                        </div>
                        <button class="card-fav-btn" onclick="toggleFav(event, this)">🤍</button>
                    </div>
                    <div class="card-body">
                        <div class="card-header-row">
                            <h3 class="restaurant-name">${r.name}</h3>
                            <div class="rating-badge">★ ${r.rating}</div>
                        </div>
                        <div class="card-cuisines">${r.cuisineTags.join(', ')}</div>
                        <div class="card-meta-row">
                            <span>📍 ${r.locality.split(',')[0]}</span>
                            <span>⚡ ${r.time} • ${r.costForTwo}</span>
                        </div>
                    </div>
                </div>
            `).join('');
        }

        function toggleFav(e, btn) {
            e.stopPropagation();
            btn.textContent = (btn.textContent === '🤍') ? '❤️' : '🤍';
        }

        /* ==========================================================
           6. RESTAURANT MENU MODAL
           ========================================================== */
        function openRestaurantModal(restId) {
            const rest = RESTAURANTS.find(r => r.id === restId);
            if (!rest) return;

            document.getElementById('modalHeroImg').src = rest.img;
            document.getElementById('modalRestName').textContent = rest.name;
            document.getElementById('modalRestCuisines').textContent = `${rest.cuisineTags.join(', ')} • ${rest.costForTwo}`;
            document.getElementById('modalRestStats').textContent = `⭐ ${rest.rating} • ${rest.time} • Cash on Delivery ONLY`;

            const targetPill = document.getElementById('modalDeliveryTarget');
            const iconPill = document.getElementById('modalDeliveryIcon');
            if (deliveryMode === 'train') {
                iconPill.textContent = '🚆';
                targetPill.textContent = `${trainDetails.trainNo.split(' ')[0]} (${trainDetails.coach}, ${trainDetails.berth})`;
            } else if (deliveryMode === 'theater') {
                iconPill.textContent = '🍿';
                targetPill.textContent = `${theaterDetails.multiplex.split(' - ')[0]} (${theaterDetails.seat})`;
            } else {
                iconPill.textContent = '🛵';
                targetPill.textContent = `${currentLocality.split(',')[0]}`;
            }

            renderModalDishes(rest);
            document.getElementById('restaurantModal').classList.add('open');
            document.body.style.overflow = 'hidden';
        }

        function closeModalOnBackdrop(e) {
            if (e.target === document.getElementById('restaurantModal')) {
                closeRestaurantModal();
            }
        }

        function closeRestaurantModal() {
            document.getElementById('restaurantModal').classList.remove('open');
            document.body.style.overflow = '';
        }

        function renderModalDishes(rest) {
            const container = document.getElementById('modalMenuBody');
            container.innerHTML = rest.menu.map(dish => {
                const inCart = cart[dish.id] ? cart[dish.id].qty : 0;
                return `
                    <div class="menu-dish-item">
                        <div class="dish-info">
                            <div class="dish-top-meta">
                                ${dish.veg ? '<span class="veg-symbol"></span>' : '<span class="nonveg-symbol"></span>'}
                                <span class="dish-name">${dish.name}</span>
                            </div>
                            <div class="dish-price">₹${dish.price}</div>
                            <div class="dish-desc">${dish.desc}</div>
                        </div>
                        <div class="dish-action-side">
                            <img src="${dish.img}" class="dish-img-thumb" alt="${dish.name}">
                            ${inCart === 0
                                ? `<button class="dish-add-btn" onclick="addToCart('${dish.id}')">ADD</button>`
                                : `<div class="dish-qty-stepper">
                                    <button onclick="decrementCart('${dish.id}')">−</button>
                                    <span>${inCart}</span>
                                    <button onclick="incrementCart('${dish.id}')">+</button>
                                   </div>`
                            }
                        </div>
                    </div>
                `;
            }).join('');
        }

        /* ==========================================================
           7. CART & CHECKOUT
           ========================================================== */
        function addToCart(dishId) {
            let dish = null, rest = null;
            for (let r of RESTAURANTS) {
                let d = r.menu.find(m => m.id === dishId);
                if (d) { dish = d; rest = r; break; }
            }
            if (!dish) return;

            const existingRestId = Object.values(cart)[0]?.restaurant?.id;
            if (existingRestId && existingRestId !== rest.id) {
                if (!confirm("Your cart contains items from another place. Reset cart to add fresh items from " + rest.name + "?")) {
                    return;
                }
                cart = {};
            }

            if (!cart[dishId]) {
                cart[dishId] = { dish: dish, restaurant: rest, qty: 1 };
            } else {
                cart[dishId].qty++;
            }

            updateCartUI();
            if (document.getElementById('restaurantModal').classList.contains('open')) {
                renderModalDishes(rest);
            }
        }

        function incrementCart(dishId) {
            if (cart[dishId]) {
                cart[dishId].qty++;
                updateCartUI();
                const rest = cart[dishId].restaurant;
                if (document.getElementById('restaurantModal').classList.contains('open')) renderModalDishes(rest);
            }
        }

        function decrementCart(dishId) {
            if (cart[dishId]) {
                cart[dishId].qty--;
                if (cart[dishId].qty <= 0) delete cart[dishId];
                updateCartUI();
                const rest = RESTAURANTS.find(r => r.menu.some(m => m.id === dishId));
                if (document.getElementById('restaurantModal').classList.contains('open') && rest) renderModalDishes(rest);
            }
        }

        function openCartDrawer() {
            document.getElementById('cartDrawer').classList.add('open');
            document.getElementById('cartDrawerBackdrop').classList.add('open');
            document.body.style.overflow = 'hidden';
            updateCartUI();
        }

        function closeCartDrawer() {
            document.getElementById('cartDrawer').classList.remove('open');
            document.getElementById('cartDrawerBackdrop').classList.remove('open');
            document.body.style.overflow = '';
        }

        function updateCartUI() {
            const items = Object.values(cart);
            const countBadge = document.getElementById('cartCountBadge');
            const totalCount = items.reduce((acc, i) => acc + i.qty, 0);
            countBadge.textContent = totalCount;

            const body = document.getElementById('drawerBody');
            const footer = document.getElementById('drawerFooter');

            if (items.length === 0) {
                body.innerHTML = `
                    <div style="text-align:center; padding:60px 20px;">
                        <div style="font-size:54px; margin-bottom:12px;">🛒</div>
                        <h4 style="font-size:18px; margin-bottom:6px;">Your cart is empty</h4>
                        <p style="font-size:13px; color:#64748B; margin-bottom:16px;">Add ice creams, waffles, hot samosas or biryanis to feast!</p>
                        <button onclick="closeCartDrawer()" style="background:var(--tomato-red); color:white; padding:8px 20px; border-radius:var(--radius-full); font-weight:700;">Explore Menu</button>
                    </div>
                `;
                footer.innerHTML = '';
                return;
            }

            const itemSubtotal = items.reduce((acc, i) => acc + (i.dish.price * i.qty), 0);
            let discount = 0;
            if (appliedCoupon) {
                discount = Math.min(appliedCoupon.flat, itemSubtotal * appliedCoupon.discountPct);
            }
            const deliveryFee = 35;
            const platformFee = 5;
            const taxes = Math.round(itemSubtotal * 0.05);
            const grandTotal = Math.max(0, Math.round(itemSubtotal - discount + deliveryFee + platformFee + taxes));

            let destinationCardHTML = '';
            if (deliveryMode === 'train') {
                destinationCardHTML = `
                    <div class="cart-target-destination-card">
                        <div>
                            <strong>🚆 Train Delivery: ${trainDetails.trainNo.split(' ')[0]}</strong>
                            <div style="font-size:11.5px; color:#0369A1;">Station: ${trainDetails.station} • ${trainDetails.coach}, ${trainDetails.berth}</div>
                        </div>
                        <button onclick="switchDeliveryMode('train')" style="background:#E0F2FE; color:#0369A1; padding:4px 8px; border-radius:4px; font-size:11px; font-weight:800;">Edit Seat</button>
                    </div>
                `;
            } else if (deliveryMode === 'theater') {
                destinationCardHTML = `
                    <div class="cart-target-destination-card mode-theater-card">
                        <div>
                            <strong>🍿 Cinema Delivery: ${theaterDetails.multiplex.split(' - ')[0]}</strong>
                            <div style="font-size:11.5px; color:#6B21A8;">Screen: ${theaterDetails.audi} • Seat: ${theaterDetails.seat}</div>
                        </div>
                        <button onclick="switchDeliveryMode('theater')" style="background:#F3E8FF; color:#6B21A8; padding:4px 8px; border-radius:4px; font-size:11px; font-weight:800;">Edit Seat</button>
                    </div>
                `;
            } else {
                destinationCardHTML = `
                    <div class="cart-target-destination-card mode-doorstep-card">
                        <div>
                            <strong>🛵 Doorstep Delivery</strong>
                            <div style="font-size:11.5px; color:#BE123C;">Delivering to: ${currentLocality}</div>
                        </div>
                    </div>
                `;
            }

            body.innerHTML = `
                ${destinationCardHTML}

                <!-- Items List -->
                <div style="margin-bottom: 20px;">
                    ${items.map(i => `
                        <div class="cart-item-row">
                            <div>
                                <div class="cart-item-name">${i.dish.name}</div>
                                <div style="font-size:12px; color:#64748B;">₹${i.dish.price} × ${i.qty} = ₹${i.dish.price * i.qty}</div>
                            </div>
                            <div class="dish-qty-stepper" style="margin-top:0;">
                                <button onclick="decrementCart('${i.dish.id}')">−</button>
                                <span>${i.qty}</span>
                                <button onclick="incrementCart('${i.dish.id}')">+</button>
                            </div>
                        </div>
                    `).join('')}
                </div>

                <!-- Coupon Box -->
                <div class="coupon-box">
                    <input type="text" id="couponInput" placeholder="Try: GOLDENGOAT, SPIN50" value="${appliedCoupon ? appliedCoupon.code : ''}">
                    <button class="coupon-apply-btn" onclick="applyManualCoupon()">${appliedCoupon ? 'Applied ✓' : 'Apply'}</button>
                </div>

                <!-- Bill -->
                <div class="bill-section">
                    <div class="bill-line"><span>Item Total</span><span>₹${itemSubtotal}</span></div>
                    ${appliedCoupon ? `<div class="bill-line" style="color:#10B981; font-weight:700;"><span>Coupon Discount (${appliedCoupon.code})</span><span>-₹${Math.round(discount)}</span></div>` : ''}
                    <div class="bill-line"><span>Delivery Partner Fee</span><span>₹${deliveryFee}</span></div>
                    <div class="bill-line"><span>Platform Fee</span><span>₹${platformFee}</span></div>
                    <div class="bill-line"><span>GST (5%)</span><span>₹${taxes}</span></div>
                    <div class="bill-line total"><span>To Pay (Cash on Delivery)</span><span>₹${grandTotal}</span></div>
                </div>

                <div class="payment-notice-card">
                    <strong>💵 CASH ON DELIVERY ONLY</strong>
                    <p style="margin-top:2px;">Please keep exact cash ready. (Feeding cash notes to the goat courier is strictly prohibited).</p>
                </div>
            `;

            footer.innerHTML = `
                <button class="checkout-btn" onclick="launchPrankOrderSequence(${grandTotal})">
                    <span>Place Order (Cash on Delivery) 💵</span>
                    <span>₹${grandTotal} ➔</span>
                </button>
            `;
        }

        function applyManualCoupon() {
            const val = document.getElementById('couponInput').value.trim().toUpperCase();
            if (!val) return;
            if (val === 'GOLDENGOAT') appliedCoupon = { code: val, discountPct: 1.0, flat: 500 };
            else if (val === 'ARCADE60') appliedCoupon = { code: val, discountPct: 0.6, flat: 250 };
            else if (val === 'GOAT70') appliedCoupon = { code: val, discountPct: 0.7, flat: 300 };
            else if (val === 'SPIN50') appliedCoupon = { code: val, discountPct: 0.5, flat: 150 };
            else appliedCoupon = { code: val, discountPct: 0.3, flat: 100 };

            updateCartUI();
            alert(`Coupon "${val}" applied successfully! 🍅`);
        }

        /* ==========================================================
           8. THE PRANK & MULTIPLE CARTOON GOAT MEMES SEQUENCE
           ========================================================== */
        const MEMES_DATA = {
            'delivery_cartoon': {
                img: 'cartoon_goat_delivery.jpg',
                footer: 'I AM DRIFTING MY TURBO SCOOTER AND ATE HALF YOUR FRIES! MEEEEHHH!',
                comment: 'Billy Courier: "Your food was so delicious on the scooter that I had to conduct a mandatory 3-bite quality audit. Approved! 10/10!"'
            },
            'chef_cartoon': {
                img: 'cartoon_goat_meme.jpg',
                footer: 'BAAAAAAAH! CHEF BILLY HAS PERSONALLY BLESSED YOUR FOOD!',
                comment: 'Chef Billy: "I tossed extra tomatoes and sprinkled secret chaos dust into your meal. Enjoy the fireworks! BAAAAAAH!"'
            },
            'real_goat': {
                img: 'goat.jpg',
                footer: 'DID YOU THINK YOU COULD GET CASH ON DELIVERY WITHOUT THE GOAT?! 📢 BAAAAAAH!',
                comment: 'Real Billy: "I stared into your soul through the screen. Prepare the exact cash notes, my hooves cannot hold coins!"'
            }
        };

        let currentActiveMeme = 'delivery_cartoon';

        function switchMeme(memeKey) {
            currentActiveMeme = memeKey;
            document.getElementById('memeTab1').classList.toggle('active', memeKey === 'delivery_cartoon');
            document.getElementById('memeTab2').classList.toggle('active', memeKey === 'chef_cartoon');
            document.getElementById('memeTab3').classList.toggle('active', memeKey === 'real_goat');

            const data = MEMES_DATA[memeKey];
            document.getElementById('activeMemeImg').src = data.img;
            document.getElementById('activeMemeFooter').textContent = data.footer;
            document.getElementById('billyRandomFunComment').textContent = data.comment;
            playCartoonBleat();
        }

        function launchPrankOrderSequence(totalAmount) {
            closeCartDrawer();
            if (document.getElementById('restaurantModal').classList.contains('open')) {
                closeRestaurantModal();
            }

            const prankWrap = document.getElementById('prankModalWrap');
            const loader = document.getElementById('prankLoader');
            const memeCard = document.getElementById('memeRevealCard');
            const liveTracker = document.getElementById('liveTrackerCard');
            const siren = document.getElementById('sirenFlash');

            prankWrap.classList.add('open');
            loader.style.display = 'block';
            memeCard.style.display = 'none';
            liveTracker.style.display = 'none';
            siren.classList.remove('active');
            document.body.classList.remove('screen-shake');

            // Destination customized loader texts
            const statusText = document.getElementById('loaderStatusText');
            const subText = document.getElementById('loaderSubText');

            if (deliveryMode === 'train') {
                statusText.textContent = `Tracking Train #${trainDetails.trainNo.split(' ')[0]}...`;
                subText.textContent = `Locating Platform Runner at ${trainDetails.station}...`;
            } else if (deliveryMode === 'theater') {
                statusText.textContent = `Connecting with Cinema Usher at ${theaterDetails.multiplex.split(' - ')[0]}...`;
                subText.textContent = `Timing delivery with intermission in ${theaterDetails.audi}...`;
            } else {
                statusText.textContent = `Assigning Locality Courier in ${currentLocality.split(',')[0]}...`;
                subText.textContent = `Checking goat scooter fuel and hoof tire pressure...`;
            }

            setTimeout(() => {
                statusText.textContent = "Verifying Cash on Delivery Mode...";
                subText.textContent = "Preparing exact change, hot sauce and goat snacks...";
            }, 1100);

            // Trigger Prank Reveal
            setTimeout(() => {
                loader.style.display = 'none';
                playRealGoatSound();

                siren.classList.add('active');
                document.body.classList.add('screen-shake');
                memeCard.style.display = 'flex';

                // Pick destination specific initial meme comment
                if (deliveryMode === 'train') {
                    document.getElementById('billyCommentTitle').textContent = `Platform Runner Billy says:`;
                    document.getElementById('billyRandomFunComment').textContent = `Train #${trainDetails.trainNo.split(' ')[0]} stops for only 4 minutes at ${trainDetails.station}! I am currently sprinting down the platform jumping over luggage to reach ${trainDetails.coach}, ${trainDetails.berth}! Hold tight! BAAAAAAH!`;
                } else if (deliveryMode === 'theater') {
                    document.getElementById('billyCommentTitle').textContent = `Cinema Usher Billy says:`;
                    document.getElementById('billyRandomFunComment').textContent = `I snuck into ${theaterDetails.audi} wearing 3D glasses! I am currently sitting in the dark near ${theaterDetails.seat} guarding your food. Do not sneeze or the villain will hear us! BAAAAAAH!`;
                }

                if (typeof confetti === 'function') {
                    confetti({ particleCount: 130, spread: 90, origin: { y: 0.55 } });
                }

                setTimeout(() => {
                    siren.classList.remove('active');
                    document.body.classList.remove('screen-shake');
                }, 1200);

            }, 2100);
        }

        function showLiveTracker() {
            document.getElementById('memeRevealCard').style.display = 'none';
            const trackerCard = document.getElementById('liveTrackerCard');
            trackerCard.style.display = 'flex';

            const orderId = '#TOM-' + Math.floor(10000 + Math.random() * 89999);
            document.getElementById('trackerOrderId').textContent = orderId;

            const targetInfo = document.getElementById('trackerDeliveryTargetInfo');
            const mapPin = document.getElementById('mapTargetPin');
            const mapPill = document.getElementById('mapStatusPill');
            const agentName = document.getElementById('trackerAgentName');

            if (deliveryMode === 'train') {
                targetInfo.innerHTML = `🚆 <strong>Train Delivery:</strong> Train #${trainDetails.trainNo} • Station: ${trainDetails.station} • ${trainDetails.coach}, ${trainDetails.berth}`;
                mapPin.textContent = '🚆📍';
                mapPill.textContent = `Status: Sprinting on Platform 3 to reach Coach ${trainDetails.coach.split(' ')[0]}!`;
                agentName.textContent = `Birju "The Train Runner"`;
            } else if (deliveryMode === 'theater') {
                targetInfo.innerHTML = `🍿 <strong>Cinema Delivery:</strong> ${theaterDetails.multiplex} • ${theaterDetails.audi} • Seat ${theaterDetails.seat}`;
                mapPin.textContent = '🎬🍿';
                mapPill.textContent = `Status: Stealthily entering ${theaterDetails.audi} with your food tray!`;
                agentName.textContent = `Bunty "The Cinema Usher"`;
            } else {
                targetInfo.innerHTML = `🛵 <strong>Doorstep Delivery:</strong> ${currentLocality}`;
                mapPin.textContent = '🏠📍';
                mapPill.textContent = `Status: Trotting along highway at 42 km/h`;
                agentName.textContent = `Billy "The Screaming Goat"`;
            }
        }

        function closePrankAndReset() {
            document.getElementById('prankModalWrap').classList.remove('open');
            cart = {};
            appliedCoupon = null;
            updateCartUI();
            renderRestaurants();
        }

        window.addEventListener('DOMContentLoaded', initApp);
    </script>
</body>

</html>
'''

with open('index3.html', 'w', encoding='utf-8') as f:
    f.write(app_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(app_html)

print("Successfully generated and saved index3.html and index.html!")
