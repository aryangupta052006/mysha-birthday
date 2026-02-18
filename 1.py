from flask import Flask, render_template_string, send_file, jsonify, request, session, send_from_directory
import os
import base64
from datetime import datetime, timedelta
import random
import json
import math

app = Flask(__name__)
app.secret_key = 'mysha_birthday_secret_2026_super_enhanced'

# Allow all hosts for development
app.config['SERVER_NAME'] = None
app.config['PREFERRED_URL_SCHEME'] = 'http'

# Enhanced HTML Template with advanced features
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎂 Happy Birthday Mysha! - The Queen's Special Day 🎂</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:wght@400;700;900&family=Poppins:wght@300;400;600;700&family=Dancing+Script:wght@400;700&family=Pacifico&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
        }
        
        /* Floating Particles Background */
        .particles {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
            pointer-events: none;
        }
        
        .particle {
            position: absolute;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.5);
            animation: float 15s infinite linear;
        }
        
        @keyframes float {
            0% {
                transform: translateY(100vh) scale(0);
                opacity: 0;
            }
            10% {
                opacity: 1;
            }
            90% {
                opacity: 1;
            }
            100% {
                transform: translateY(-100vh) scale(1);
                opacity: 0;
            }
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
            position: relative;
            z-index: 1;
        }
        
        /* Enhanced Navigation */
        .nav-bar {
            position: fixed;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(255, 255, 255, 0.25);
            backdrop-filter: blur(10px);
            padding: 15px 30px;
            border-radius: 50px;
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
            justify-content: center;
            z-index: 1000;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2),
                        0 0 0 2px rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.3);
        }
        
        .nav-btn {
            padding: 12px 25px;
            border: none;
            border-radius: 40px;
            background: linear-gradient(135deg, rgba(255,255,255,0.2), rgba(255,255,255,0.1));
            color: white;
            cursor: pointer;
            font-size: 16px;
            font-weight: 600;
            letter-spacing: 0.5px;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255,255,255,0.3);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        /* Open Button Style */
        .open-btn {
            background: linear-gradient(135deg, gold, #ffd700, #ffa500);
            color: #333;
            font-size: 1.8rem;
            font-weight: bold;
            padding: 20px 50px;
            border: none;
            border-radius: 60px;
            cursor: pointer;
            margin-top: 30px;
            box-shadow: 0 10px 30px rgba(255,215,0,0.5);
            transition: all 0.3s;
            border: 2px solid white;
            animation: pulse 1.5s infinite;
        }

        .open-btn:hover {
            transform: scale(1.1);
            box-shadow: 0 20px 40px gold;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        
        .nav-btn:hover {
            transform: translateY(-5px) scale(1.05);
            background: linear-gradient(135deg, rgba(255,255,255,0.4), rgba(255,255,255,0.2));
            box-shadow: 0 15px 30px rgba(0,0,0,0.3),
                        0 0 20px rgba(255,215,0,0.3);
            border-color: gold;
        }
        
        .nav-btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border-radius: 40px;
            background: linear-gradient(135deg, rgba(255,215,0,0.3), rgba(255,105,180,0.3));
            opacity: 0;
            transition: opacity 0.3s;
            z-index: -1;
        }
        
        .nav-btn:hover::before {
            opacity: 1;
        }
        
        /* Pages */
        .page {
            display: none;
            min-height: 100vh;
            padding: 120px 20px 40px;
            animation: pageEnter 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        }
        
        .page.active {
            display: block;
        }
        
        @keyframes pageEnter {
            0% {
                opacity: 0;
                transform: scale(0.9) translateY(50px);
            }
            100% {
                opacity: 1;
                transform: scale(1) translateY(0);
            }
        }
        
        /* Enhanced Home Page */
        .home-content {
            text-align: center;
            padding: 50px 20px;
            position: relative;
        }
        
        .floating-hearts {
            position: absolute;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            pointer-events: none;
        }
        
        .heart {
            position: absolute;
            font-size: 20px;
            color: rgba(255, 105, 180, 0.6);
            animation: heartFloat 6s ease-in-out infinite;
        }
        
        @keyframes heartFloat {
            0% {
                transform: translateY(100vh) rotate(0deg);
                opacity: 0;
            }
            50% {
                opacity: 1;
            }
            100% {
                transform: translateY(-100vh) rotate(360deg);
                opacity: 0;
            }
        }
        
        .birthday-title {
            font-size: 5rem;
            font-family: 'Great Vibes', cursive;
            background: linear-gradient(135deg, #ffd700, #ffa500, #ff69b4, #ff1493);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 30px rgba(255,215,0,0.5),
                         0 0 60px rgba(255,105,180,0.3);
            margin-bottom: 20px;
            animation: titleGlow 3s ease-in-out infinite;
            letter-spacing: 2px;
        }
        
        @keyframes titleGlow {
            0%, 100% {
                filter: drop-shadow(0 0 20px rgba(255,215,0,0.5));
            }
            50% {
                filter: drop-shadow(0 0 40px rgba(255,20,147,0.8));
            }
        }
        
        .name-large {
            font-size: 8rem;
            font-family: 'Playfair Display', serif;
            font-weight: 900;
            background: linear-gradient(135deg, #fff, #ffd700, #ff69b4, #fff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.3),
                         0 0 30px rgba(255,215,0,0.5),
                         0 0 60px rgba(255,105,180,0.3);
            margin: 30px 0;
            animation: namePulse 2s ease-in-out infinite;
            transform-style: preserve-3d;
            perspective: 1000px;
        }
        
        @keyframes namePulse {
            0%, 100% {
                transform: scale(1) rotateX(0deg);
            }
            50% {
                transform: scale(1.05) rotateX(5deg);
            }
        }
        
        /* 3D Cake Animation */
        .cake-3d {
            position: relative;
            width: 300px;
            height: 300px;
            margin: 50px auto;
            transform-style: preserve-3d;
            animation: cakeSpin 20s infinite linear;
        }
        
        @keyframes cakeSpin {
            0% {
                transform: rotateY(0deg) rotateX(10deg);
            }
            100% {
                transform: rotateY(360deg) rotateX(10deg);
            }
        }
        
        .cake-layer {
            position: absolute;
            width: 200px;
            height: 60px;
            left: 50%;
            transform: translateX(-50%);
            border-radius: 20px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        }
        
        .layer1 {
            bottom: 0;
            background: linear-gradient(135deg, #f5d0a9, #e6b87e);
            width: 250px;
            height: 80px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.3),
                       0 0 0 5px #fff,
                       0 0 0 8px #f5d0a9;
        }
        
        .layer2 {
            bottom: 70px;
            background: linear-gradient(135deg, #f5b7b1, #f1948a);
            width: 220px;
            height: 70px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.3),
                       0 0 0 5px #fff,
                       0 0 0 8px #f5b7b1;
        }
        
        .layer3 {
            bottom: 130px;
            background: linear-gradient(135deg, #d7bde2, #c39bd3);
            width: 190px;
            height: 60px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.3),
                       0 0 0 5px #fff,
                       0 0 0 8px #d7bde2;
        }
        
        .candle {
            position: absolute;
            bottom: 180px;
            left: 50%;
            transform: translateX(-50%);
            width: 30px;
            height: 100px;
            background: linear-gradient(135deg, #fff5e6, #ffe4cc);
            border-radius: 15px 15px 5px 5px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }
        
        .flame {
            position: absolute;
            bottom: 270px;
            left: 50%;
            transform: translateX(-50%);
            width: 20px;
            height: 40px;
            background: radial-gradient(circle at 50% 0%, #ffff00, #ff9900, #ff5500);
            border-radius: 50% 50% 20% 20%;
            animation: flicker 0.5s ease-in-out infinite;
            filter: blur(1px);
            box-shadow: 0 -10px 30px #ff9900,
                        0 -20px 40px #ff5500;
        }
        
        @keyframes flicker {
            0%, 100% {
                transform: translateX(-50%) scale(1);
                opacity: 1;
            }
            25% {
                transform: translateX(-50%) scale(1.1) rotate(-2deg);
                opacity: 0.9;
            }
            75% {
                transform: translateX(-50%) scale(0.9) rotate(2deg);
                opacity: 0.8;
            }
        }
        
        .drama-btn {
            padding: 25px 70px;
            font-size: 2.5rem;
            font-weight: bold;
            background: linear-gradient(135deg, #ff6b6b, #ff4757, #ff3838);
            color: white;
            border: none;
            border-radius: 80px;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 10px 30px rgba(255,71,87,0.4),
                        0 20px 40px rgba(255,71,87,0.2),
                        0 0 0 2px rgba(255,255,255,0.3);
            letter-spacing: 2px;
            position: relative;
            overflow: hidden;
        }
        
        .drama-btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            transition: left 0.5s;
        }
        
        .drama-btn:hover::before {
            left: 100%;
        }
        
        .drama-btn:hover {
            transform: scale(1.15) translateY(-10px);
            box-shadow: 0 20px 50px rgba(255,71,87,0.6),
                        0 30px 60px rgba(255,71,87,0.4),
                        0 0 0 4px rgba(255,255,255,0.5);
        }
        
        /* Enhanced Memory Lane */
        .memory-section {
            position: relative;
        }
        
        .memory-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 40px;
            margin-top: 60px;
            perspective: 2000px;
        }
        
        .memory-card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 30px;
            overflow: hidden;
            box-shadow: 0 20px 40px rgba(0,0,0,0.3),
                        0 0 0 2px rgba(255,255,255,0.3),
                        0 0 20px rgba(255,215,0,0.2);
            transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            transform-style: preserve-3d;
            cursor: pointer;
            position: relative;
        }
        
        .memory-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(255,215,0,0.2), rgba(255,105,180,0.2));
            opacity: 0;
            transition: opacity 0.3s;
            pointer-events: none;
        }
        
        .memory-card:hover {
            transform: translateY(-20px) rotateX(5deg) rotateY(5deg);
            box-shadow: 0 40px 80px rgba(0,0,0,0.4),
                        0 0 0 4px rgba(255,255,255,0.5),
                        0 0 40px rgba(255,215,0,0.4);
        }
        
        .memory-card:hover::before {
            opacity: 1;
        }
        
        .memory-img {
            width: 100%;
            height: 300px;
            object-fit: cover;
            transition: transform 0.5s;
        }
        
        .memory-card:hover .memory-img {
            transform: scale(1.1);
        }
        
        .memory-quote {
            padding: 25px;
            font-size: 1.2rem;
            font-style: italic;
            color: #333;
            text-align: center;
            font-family: 'Dancing Script', cursive;
            font-size: 1.4rem;
            background: linear-gradient(135deg, #fff9f9, #fff);
            position: relative;
        }
        
        .memory-quote::before {
            content: '"';
            font-size: 4rem;
            color: rgba(255,105,180,0.3);
            position: absolute;
            top: -10px;
            left: 10px;
        }
        
        .memory-quote::after {
            content: '"';
            font-size: 4rem;
            color: rgba(255,105,180,0.3);
            position: absolute;
            bottom: -30px;
            right: 10px;
        }
        
        /* Enhanced Secret Message */
        .secret-container {
            max-width: 800px;
            margin: 50px auto;
            text-align: center;
            perspective: 2000px;
        }
        
        .locked-message {
            background: linear-gradient(135deg, #667eea, #764ba2, #ff6b6b);
            color: white;
            padding: 60px;
            border-radius: 40px;
            cursor: pointer;
            transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 20px 40px rgba(0,0,0,0.3),
                        0 0 0 3px rgba(255,255,255,0.3),
                        0 0 40px rgba(102,126,234,0.4);
            position: relative;
            overflow: hidden;
            border: 2px solid rgba(255,255,255,0.3);
        }
        
        .locked-message::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, rgba(255,255,255,0.3), transparent);
            transform: rotate(45deg);
            animation: shimmer 3s infinite;
        }
        
        @keyframes shimmer {
            0% {
                transform: translateX(-100%) rotate(45deg);
            }
            100% {
                transform: translateX(100%) rotate(45deg);
            }
        }
        
        .locked-message:hover {
            transform: scale(1.05) translateY(-10px);
            box-shadow: 0 30px 60px rgba(102,126,234,0.6),
                        0 0 0 5px rgba(255,255,255,0.5),
                        0 0 60px gold;
        }
        
        .emotional-message {
            display: none;
            background: rgba(255, 255, 255, 0.98);
            padding: 60px;
            border-radius: 40px;
            margin-top: 30px;
            font-size: 1.3rem;
            line-height: 2;
            color: #333;
            white-space: pre-line;
            box-shadow: 0 20px 40px rgba(0,0,0,0.2),
                        0 0 0 2px gold,
                        0 0 40px rgba(255,215,0,0.3);
            animation: messageReveal 1s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            text-align: left;
            position: relative;
            font-family: 'Playfair Display', serif;
            border: 2px solid rgba(255,215,0,0.3);
        }
        
        @keyframes messageReveal {
            0% {
                opacity: 0;
                transform: scale(0.8) rotateX(-20deg);
            }
            100% {
                opacity: 1;
                transform: scale(1) rotateX(0);
            }
        }
        
        .emotional-message::first-letter {
            font-size: 4rem;
            font-family: 'Great Vibes', cursive;
            color: #ff6b6b;
            float: left;
            line-height: 1;
            margin-right: 10px;
        }
        
        /* Enhanced Video Section */
        .video-wrapper {
            position: relative;
            max-width: 1000px;
            margin: 0 auto;
            border-radius: 40px;
            overflow: hidden;
            box-shadow: 0 30px 60px rgba(0,0,0,0.4),
                        0 0 0 4px rgba(255,255,255,0.3),
                        0 0 50px rgba(255,215,0,0.3);
        }
        
        .video-container {
            position: relative;
            padding-bottom: 56.25%;
            height: 0;
        }
        
        .video-container iframe,
        .video-container video {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
        }
        
        .video-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(255,105,180,0.2), rgba(102,126,234,0.2));
            pointer-events: none;
            mix-blend-mode: overlay;
        }
        
        /* Enhanced Game Section */
        .game-container {
            max-width: 800px;
            margin: 0 auto;
            text-align: center;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 50px;
            border-radius: 60px;
            box-shadow: 0 30px 60px rgba(0,0,0,0.3),
                        0 0 0 3px rgba(255,255,255,0.2);
        }
        
        .jethalal-3d {
            width: 250px;
            height: 250px;
            margin: 30px auto;
            position: relative;
            transform-style: preserve-3d;
            animation: jethaDance 4s ease-in-out infinite;
            cursor: pointer;
        }
        
        @keyframes jethaDance {
            0%, 100% {
                transform: rotateY(0deg) rotateX(0deg) translateY(0);
            }
            25% {
                transform: rotateY(10deg) rotateX(5deg) translateY(-20px);
            }
            50% {
                transform: rotateY(0deg) rotateX(-5deg) translateY(0);
            }
            75% {
                transform: rotateY(-10deg) rotateX(5deg) translateY(-20px);
            }
        }
        
        .jethalal-face {
            width: 100%;
            height: 100%;
            background: radial-gradient(circle at 30% 30%, #ffb347, #ff8c00);
            border-radius: 50%;
            position: relative;
            box-shadow: 0 20px 40px rgba(0,0,0,0.3),
                        0 0 0 5px #fff,
                        0 0 0 8px #ff8c00;
        }
        
        .eyes {
            position: absolute;
            top: 30%;
            width: 100%;
            display: flex;
            justify-content: space-around;
            padding: 0 50px;
        }
        
        .eye {
            width: 30px;
            height: 40px;
            background: white;
            border-radius: 50%;
            position: relative;
            animation: blink 3s infinite;
        }
        
        @keyframes blink {
            0%, 46%, 50%, 100% {
                transform: scaleY(1);
            }
            48% {
                transform: scaleY(0.1);
            }
        }
        
        .eye::after {
            content: '';
            position: absolute;
            top: 30%;
            left: 30%;
            width: 40%;
            height: 40%;
            background: #333;
            border-radius: 50%;
        }
        
        .mouth {
            position: absolute;
            bottom: 25%;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 30px;
            background: #ff6b6b;
            border-radius: 0 0 50px 50px;
            overflow: hidden;
        }
        
        .mouth::after {
            content: '';
            position: absolute;
            top: -10px;
            left: 0;
            width: 100%;
            height: 20px;
            background: #ff8787;
            border-radius: 50%;
        }
        
        .game-stats {
            display: flex;
            justify-content: center;
            gap: 40px;
            margin: 30px 0;
            font-size: 1.5rem;
            color: white;
        }
        
        .game-score, .game-attempts {
            background: rgba(255,255,255,0.2);
            padding: 15px 30px;
            border-radius: 50px;
            backdrop-filter: blur(5px);
            border: 2px solid rgba(255,255,255,0.3);
        }
        
        .game-btn {
            padding: 18px 40px;
            font-size: 1.3rem;
            background: linear-gradient(135deg, #4CAF50, #45a049, #2e7d32);
            color: white;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            margin: 15px;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 10px 20px rgba(0,0,0,0.3),
                        0 0 0 2px rgba(255,255,255,0.2);
            font-weight: bold;
            letter-spacing: 1px;
            position: relative;
            overflow: hidden;
        }
        
        .game-btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            transition: left 0.5s;
        }
        
        .game-btn:hover::before {
            left: 100%;
        }
        
        .game-btn:hover {
            transform: scale(1.1) translateY(-5px);
            box-shadow: 0 20px 40px rgba(76,175,80,0.4),
                        0 0 0 4px rgba(255,255,255,0.4);
        }
        
        /* Enhanced Gift Section */
        .gift-showcase {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 40px;
        }
        
        .scratch-card {
            width: 400px;
            height: 500px;
            margin: 20px auto;
            position: relative;
            cursor: pointer;
            perspective: 2000px;
        }
        
        .scratch-card-inner {
            position: relative;
            width: 100%;
            height: 100%;
            text-align: center;
            transition: transform 1s;
            transform-style: preserve-3d;
        }
        
        .scratch-card:hover .scratch-card-inner {
            transform: rotateY(10deg) rotateX(5deg);
        }
        
        .scratch-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #808080, #a9a9a9, #696969);
            background-image: repeating-linear-gradient(45deg, 
                rgba(255,255,255,0.1) 0px, 
                rgba(255,255,255,0.1) 10px,
                rgba(0,0,0,0.1) 10px,
                rgba(0,0,0,0.1) 20px);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            font-weight: bold;
            color: white;
            border-radius: 30px;
            transition: opacity 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 20px 40px rgba(0,0,0,0.4),
                        0 0 0 4px gold,
                        0 0 40px rgba(255,215,0,0.4);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            backdrop-filter: blur(2px);
            z-index: 2;
        }
        
        .gift-content {
            background: linear-gradient(135deg, #fff, #fff9f9);
            width: 100%;
            height: 100%;
            border-radius: 30px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.3),
                        0 0 0 4px gold,
                        0 0 60px rgba(255,215,0,0.3);
            position: relative;
            overflow: hidden;
        }
        
        .gift-content::before {
            content: '🎁';
            font-size: 8rem;
            position: absolute;
            opacity: 0.1;
            transform: rotate(-15deg);
            bottom: -20px;
            right: -20px;
        }
        
        .countdown-timer {
            font-size: 3rem;
            color: #ff6b6b;
            margin: 30px 0;
            font-family: 'Playfair Display', serif;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2),
                         0 0 20px gold;
            background: rgba(255,255,255,0.9);
            padding: 20px 40px;
            border-radius: 60px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        .coupons {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 30px;
            margin: 40px 0;
            width: 100%;
        }
        
        .coupon-card {
            background: linear-gradient(135deg, #ffd700, #ffa500, #ff8c00);
            padding: 30px 20px;
            border-radius: 20px;
            text-align: center;
            color: white;
            font-weight: bold;
            font-size: 1.3rem;
            transform: rotate(-2deg) scale(1);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 15px 30px rgba(0,0,0,0.3),
                        0 0 0 3px rgba(255,255,255,0.3),
                        0 0 30px rgba(255,215,0,0.3);
            position: relative;
            overflow: hidden;
            cursor: pointer;
        }
        
        .coupon-card:nth-child(even) {
            transform: rotate(2deg) scale(1);
        }
        
        .coupon-card:hover {
            transform: rotate(0deg) scale(1.1) translateY(-10px);
            box-shadow: 0 25px 50px rgba(0,0,0,0.4),
                        0 0 0 5px rgba(255,255,255,0.5),
                        0 0 50px gold;
        }
        
        .coupon-card::before {
            content: '🎫';
            font-size: 3rem;
            position: absolute;
            top: -10px;
            left: -10px;
            opacity: 0.2;
            transform: rotate(-15deg);
        }
        
        /* Enhanced Favorite Page */
        .favorite-container {
            text-align: center;
            max-width: 800px;
            margin: 0 auto;
        }
        
        .vinyl-record {
            width: 400px;
            height: 400px;
            margin: 40px auto;
            position: relative;
            animation: spin 10s linear infinite;
            cursor: pointer;
        }
        
        @keyframes spin {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        
        .vinyl {
            width: 100%;
            height: 100%;
            background: radial-gradient(circle at 30% 30%, #333, #111);
            border-radius: 50%;
            box-shadow: 0 20px 40px rgba(0,0,0,0.5),
                        0 0 0 5px #444,
                        0 0 0 10px #666,
                        0 0 0 15px #888,
                        0 0 50px rgba(255,215,0,0.3);
            position: relative;
        }
        
        .vinyl::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 80px;
            height: 80px;
            background: radial-gradient(circle, #ffd700, #ffa500);
            border-radius: 50%;
            box-shadow: 0 0 30px gold;
        }
        
        .vinyl::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: repeating-radial-gradient(circle at 50% 50%, 
                transparent 0px, 
                transparent 5px, 
                rgba(255,255,255,0.1) 5px, 
                rgba(255,255,255,0.1) 10px);
            border-radius: 50%;
        }
        
        .song-title-enhanced {
            font-size: 2.5rem;
            color: white;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3),
                        0 0 20px gold,
                        0 0 40px hotpink;
            margin: 30px 0;
            font-family: 'Great Vibes', cursive;
        }
        
        .audio-controls-enhanced {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin: 30px 0;
        }
        
        .audio-btn-enhanced {
            padding: 20px 50px;
            border: none;
            border-radius: 60px;
            background: linear-gradient(135deg, #ff6b6b, #ff4757, #ff3838);
            color: white;
            cursor: pointer;
            font-size: 1.3rem;
            font-weight: bold;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 10px 20px rgba(0,0,0,0.3),
                        0 0 0 3px rgba(255,255,255,0.2);
        }
        
        .audio-btn-enhanced:hover {
            transform: scale(1.15) translateY(-5px);
            box-shadow: 0 20px 40px rgba(255,71,87,0.4),
                        0 0 0 5px rgba(255,255,255,0.4);
        }
        
        .cute-quote-enhanced {
            font-size: 2rem;
            font-family: 'Dancing Script', cursive;
            color: white;
            margin: 50px 0;
            padding: 40px;
            background: rgba(255,255,255,0.2);
            backdrop-filter: blur(10px);
            border-radius: 40px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.2),
                        0 0 0 3px rgba(255,255,255,0.3),
                        0 0 50px rgba(255,215,0,0.3);
            line-height: 1.6;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
        }
        
        /* Enhanced Wish Page */
        .wish-container-enhanced {
            max-width: 700px;
            margin: 40px auto;
            padding: 50px;
            background: rgba(255,255,255,0.95);
            border-radius: 60px;
            box-shadow: 0 30px 60px rgba(0,0,0,0.3),
                        0 0 0 4px gold,
                        0 0 60px rgba(255,215,0,0.3);
            position: relative;
            overflow: hidden;
        }
        
        .wish-container-enhanced::before {
            content: '✨';
            font-size: 15rem;
            position: absolute;
            top: -50px;
            right: -50px;
            opacity: 0.1;
            transform: rotate(15deg);
        }
        
        .wish-container-enhanced::after {
            content: '🌟';
            font-size: 15rem;
            position: absolute;
            bottom: -50px;
            left: -50px;
            opacity: 0.1;
            transform: rotate(-15deg);
        }
        
        .wish-title {
            font-size: 3rem;
            color: #ff6b6b;
            margin-bottom: 30px;
            font-family: 'Great Vibes', cursive;
            position: relative;
        }
        
        .wish-input-enhanced {
            width: 100%;
            padding: 20px;
            font-size: 1.2rem;
            border: 3px solid #ff6b6b;
            border-radius: 30px;
            margin: 20px 0;
            resize: vertical;
            font-family: 'Poppins', sans-serif;
            transition: all 0.3s;
        }
        
        .wish-input-enhanced:focus {
            outline: none;
            border-color: gold;
            box-shadow: 0 0 30px rgba(255,215,0,0.5);
            transform: scale(1.02);
        }
        
        .wish-btn-enhanced {
            padding: 20px 50px;
            background: linear-gradient(135deg, #ff6b6b, #ff4757);
            color: white;
            border: none;
            border-radius: 60px;
            cursor: pointer;
            font-size: 1.3rem;
            font-weight: bold;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 10px 20px rgba(0,0,0,0.3);
            margin-top: 20px;
        }
        
        .wish-btn-enhanced:hover {
            transform: scale(1.1) translateY(-5px);
            box-shadow: 0 20px 40px rgba(255,71,87,0.4),
                        0 0 0 4px gold;
        }
        
        .wish-message-enhanced {
            margin-top: 30px;
            padding: 30px;
            background: linear-gradient(135deg, #f0f0f0, #fff);
            border-radius: 30px;
            display: none;
            font-size: 1.2rem;
            border: 2px solid gold;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            position: relative;
        }
        
        /* Footer */
        .footer-enhanced {
            text-align: center;
            padding: 30px;
            color: white;
            margin-top: 50px;
            font-size: 1.2rem;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
            background: rgba(0,0,0,0.2);
            backdrop-filter: blur(5px);
            border-radius: 100px 100px 0 0;
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .birthday-title { font-size: 3rem; }
            .name-large { font-size: 4rem; }
            .nav-bar { padding: 10px; gap: 8px; }
            .nav-btn { padding: 8px 15px; font-size: 12px; }
            .drama-btn { font-size: 1.5rem; padding: 15px 30px; }
            .cake-3d { transform: scale(0.7); }
        }
        
        /* Loading Animation */
        .loader {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #667eea, #764ba2);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            transition: opacity 1s;
        }
        
        .loader-content {
            text-align: center;
            color: white;
        }
        
        .loader-spinner {
            width: 100px;
            height: 100px;
            border: 5px solid rgba(255,255,255,0.3);
            border-top-color: gold;
            border-radius: 50%;
            animation: spin 1s infinite linear;
            margin: 20px auto;
        }
        
        .loader-text {
            font-size: 2rem;
            font-family: 'Great Vibes', cursive;
            animation: pulse 1.5s infinite;
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:wght@400;700;900&family=Poppins:wght@300;400;600;700&family=Dancing+Script:wght@400;700&family=Pacifico&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Loading Screen -->
    <div id="loader" class="loader">
        <div class="loader-content">
            <div class="loader-spinner"></div>
            <div class="loader-text">Preparing something special for Mysha...</div>
        </div>
    </div>
    
    <!-- Floating Particles -->
    <div class="particles" id="particles"></div>
    
    <!-- Floating Hearts -->
    <div class="floating-hearts" id="floatingHearts"></div>
    
    <!-- Navigation -->
    <div class="nav-bar">
        <button class="nav-btn" onclick="showPage('home')">🏠 Home</button>
        <button class="nav-btn" onclick="showPage('memory')">📸 Memory Lane</button>
        <button class="nav-btn" onclick="showPage('secret')">🔐 Secret Message</button>
        <button class="nav-btn" onclick="showPage('video')">🎥 Video</button>
        <button class="nav-btn" onclick="showPage('gift')">🎁 Gift</button>
        <button class="nav-btn" onclick="showPage('favorite')">❤️ Favorite</button>
        <button class="nav-btn" onclick="showPage('wish')">✨ Birthday Wish</button>
    </div>
    
    <!-- Home Page -->
    <div id="home" class="page active">
        <div class="home-content">
            <h1 class="birthday-title">Welcome, Birthday Queen</h1>
            <div class="name-large">Mysha</div>
            
            <!-- 3D Cake -->
            <div class="cake-3d">
                <div class="cake-layer layer1"></div>
                <div class="cake-layer layer2"></div>
                <div class="cake-layer layer3"></div>
                <div class="candle"></div>
                <div class="flame"></div>
            </div>
            
            <button class="drama-btn" onclick="startDrama()">🎭 START THE DRAMA 🎭</button>
        </div>
    </div>
    
    <!-- Memory Lane -->
<div id="memory" class="page">
    <h1 style="text-align: center; color: white; margin-bottom: 40px; font-size: 4rem; font-family: 'Great Vibes', cursive;">📸 Memory Lane 📸</h1>
    <div class="memory-grid">
        
        <!-- PIC 1 -->
        <div class="memory-card" onclick="enlargeImage(this)">
            <img src="/static/pic1.jpeg" alt="Mysha 1" class="memory-img" onerror="this.onerror=null; this.src='https://via.placeholder.com/350x300/ff6b6b/ffffff?text=Mysha+1';">
            <div class="memory-quote">""Smile itna powerful ho ki bina kuch bole sab keh jaaye."" 💗</div>
        </div>
        
        <!-- PIC 2 -->
        <div class="memory-card" onclick="enlargeImage(this)">
            <img src="/static/pic2.jpeg" alt="Mysha 2" class="memory-img" onerror="this.onerror=null; this.src='https://via.placeholder.com/350x300/ff8e8e/ffffff?text=Mysha+2';">
            <div class="memory-quote">"Raat ki roshni mein bhi apni chamak alag hi hoti hai." 🎵</div>
        </div>
        
        <!-- PIC 3 -->
        <div class="memory-card" onclick="enlargeImage(this)">
            <img src="/static/pic3.jpeg" alt="Mysha 3" class="memory-img" onerror="this.onerror=null; this.src='https://via.placeholder.com/350x300/ffa07a/ffffff?text=Mysha+3';">
            <div class="memory-quote">"Confidence is the best outfit — wear it and own the moment." 🌈</div>
        </div>
        
        <!-- PIC 4 -->
        <div class="memory-card" onclick="enlargeImage(this)">
            <img src="/static/pic4.jpeg" alt="Mysha 4" class="memory-img" onerror="this.onerror=null; this.src='https://via.placeholder.com/350x300/ffb6c1/ffffff?text=Mysha+4';">
            <div class="memory-quote">"Khamosh nazron mein bhi hazaar kahaniyaan hoti hain." ✨</div>
        </div>
        
        <!-- PIC 5 -->
        <div class="memory-card" onclick="enlargeImage(this)">
            <img src="/static/pic5.jpeg" alt="Mysha 5" class="memory-img" onerror="this.onerror=null; this.src='https://via.placeholder.com/350x300/ff9999/ffffff?text=Mysha+5';">
            <div class="memory-quote">"Elegance kabhi loud nahi hoti, woh bas notice ho jaati hai." 💕</div>
        </div>
        
        <!-- PIC 6 -->
        <div class="memory-card" onclick="enlargeImage(this)">
            <img src="/static/pic6.jpeg" alt="Mysha 6" class="memory-img" onerror="this.onerror=null; this.src='https://via.placeholder.com/350x300/ffaaaa/ffffff?text=Mysha+6';">
            <div class="memory-quote">"Festive lights ke beech, sabse zyada glow tumhara hai." ☀️</div>
        </div>
        
        <!-- 9.jpeg (agar yeh bhi dalni hai) -->
        <div class="memory-card" onclick="enlargeImage(this)">
            <img src="/static/9.jpeg" alt="Mysha 9" class="memory-img" onerror="this.onerror=null; this.src='https://via.placeholder.com/350x300/ffbbbb/ffffff?text=Mysha+9';">
            <div class="memory-quote">"Simple rehkar bhi special lagna — wahi asli style hai." 🌸</div>
        </div>
        
        <!-- 10.jpeg (agar yeh bhi dalni hai) -->
        <div class="memory-card" onclick="enlargeImage(this)">
            <img src="/static/10.jpeg" alt="Mysha 10" class="memory-img" onerror="this.onerror=null; this.src='https://via.placeholder.com/350x300/ffcccc/ffffff?text=Mysha+10';">
            <div class="memory-quote">"Jahan sukoon mile, wahi sabse khoobsurat jagah hai." 🥹💖</div>
        </div>

        <!-- 11.jpeg (agar yeh bhi dalni hai) -->
        <div class="memory-card" onclick="enlargeImage(this)">
            <img src="/static/pic11.jpeg" alt="Mysha 11" class="memory-img" onerror="this.onerror=null; this.src='https://via.placeholder.com/350x300/ffcccc/ffffff?text=Mysha+11';">
            <div class="memory-quote">"Grace in every step, magic in every glance" 🥹💖</div>
        </div>

        <!-- 12.jpeg (agar yeh bhi dalni hai) -->
        <div class="memory-card" onclick="enlargeImage(this)">
            <img src="/static/pic12.jpeg" alt="Mysha 12" class="memory-img" onerror="this.onerror=null; this.src='https://via.placeholder.com/350x300/ffcccc/ffffff?text=Mysha+12';">
            <div class="memory-quote">"Masoom si smile, aur dil ko chhoo jaane wali simplicity." 🥹💖</div>
        </div>

    </div>
</div>
    
    <!-- Secret Message -->
<div id="secret" class="page">
    <div class="secret-container">
        
        <!-- Locked Message Box -->
        <div class="locked-message" id="lockedBox">
            <h2 style="font-size: 2.5rem; margin-bottom: 20px;">🔒 Secret Message 🔒</h2>
            <p style="font-size: 1.3rem;">Aapke liye ek special message hai!</p>
            <div style="font-size: 3rem; margin: 20px;">💝</div>
            
            <!-- OPEN BUTTON -->
            <button id="openSecretBtn" class="open-btn" onclick="showSecretMessage()">
                ✨ OPEN MESSAGE ✨
            </button>
        </div>
        
        <!-- Emotional Message (initially hidden) -->
        <div id="emotional-message" class="emotional-message">
            My Dearest Mysha,
            
            As the clock strikes midnight on your special day, my heart is overflowing with emotions that words can barely capture. You know that feeling when you find someone who just gets you? That's what you are to me - my person, my confidante, my sister from another mother.
            
            Remember those countless nights we stayed up talking about everything and nothing? The way we finish each other's sentences? How you know exactly what I'm thinking just by looking at my eyes? That's not just friendship - that's soulmate territory.
            
            You've been my rock when I was drowning, my light when everything was dark, my laughter when I needed it most. You've seen me at my absolute worst - messy hair, puffy eyes, broken heart - and you never judged. You just held my hand and said, "I'm here."
            
            I've watched you grow into this magnificent woman, chasing dreams with fire in your eyes and kindness in your heart. Your strength amazes me daily. Your compassion inspires me. Your laughter is my favorite sound in the world.
            
            Today, on your birthday, I want you to know that you are loved beyond measure. You are appreciated more than any words can express. You are the sister I never had but always needed. The universe became a better place the day you were born, and my life became infinitely better the day you walked into it.
            
            May your year ahead be filled with:
            - Dreams that come true
            - Love that knows no bounds
            - Success that exceeds your expectations
            - Happiness that follows you everywhere
            - And someone who loves you as much as I do (romantically, of course! 😉)
            
            Thank you for being you. Thank you for being mine. Thank you for every memory, every tear, every laugh, every moment.
            
            I love you more than all the stars in the sky, more than all the sand on all the beaches, more than all the words in all the languages.
            
            Happy Birthday, my beautiful, amazing, one-of-a-kind best friend.
            
            With all the love in the universe and beyond,
            Your forever friend ❤️
            Aryan
            
            P.S. - The best is yet to come, and I can't wait to witness every moment of it with you!
        </div>
    </div>
</div>
    
    <!-- Video Section -->
<div id="video" class="page">
    <h1 style="text-align: center; color: white; margin-bottom: 40px; font-size: 4rem; font-family: 'Great Vibes', cursive;">🎥 A Special Message For You 🎥</h1>
    <div class="video-wrapper">
        <div class="video-container">
            <video controls style="width:100%; height:100%; background:black;" preload="auto">
                <source src="/static/vid1.mp4" type="video/mp4">
                Your browser does not support the video tag.
            </video>
            <div class="video-overlay"></div>
        </div>
        <p style="text-align:center; margin-top:10px; color:white;">
            <a href="/static/vid1.mp4" style="color:gold;" download>📥 Download Video</a>
        </p>
    </div>
</div>
    
    <!-- Gift Reveal -->
    <div id="gift" class="page">
        <h1 style="text-align: center; color: white; margin-bottom: 40px; font-size: 4rem; font-family: 'Great Vibes', cursive;">🎁 Your Special Gift 🎁</h1>
        <div class="gift-showcase">
            <div class="scratch-card" onclick="scratchGift()">
                <div class="scratch-card-inner">
                    <div class="scratch-overlay" id="scratchOverlay">
                        <div style="transform: rotate(-10deg);">
                            ✨ Scratch to Reveal! ✨
                        </div>
                    </div>
                    <div class="gift-content" id="giftContent" style="display: none;">
                        <h2 style="color: #ff6b6b; font-size: 2.5rem; margin-bottom: 20px;">Happy Birthday Mysha! 🎂</h2>
                        <p style="font-size: 1.3rem; margin: 20px 0; color: #333;">Your surprise gift is waiting...</p>
                        <div style="font-size: 4rem;">🎁 💝 🎀</div>
                    </div>
                </div>
            </div>
            
            <div class="countdown-timer" id="countdown"></div>
            
            <div class="coupons">
                <div class="coupon-card" onclick="redeemCoupon('hug')">
                    🎫 FREE HUG<br>
                    <small>Redeem anytime, anywhere</small>
                </div>
                <div class="coupon-card" onclick="redeemCoupon('treat')">
                    🎫 FREE TREAT<br>
                    <small>Your choice of food/drink</small>
                </div>
                <div class="coupon-card" onclick="redeemCoupon('movie')">
                    🎫 MOVIE NIGHT<br>
                    <small>My treat, your choice</small>
                </div>
                <div class="coupon-card" onclick="redeemCoupon('shopping')">
                    🎫 SHOPPING DAY<br>
                    <small>Window shopping with fun</small>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Favorite Page -->
    <div id="favorite" class="page">
        <div class="favorite-container">
            <h1 style="color: white; margin-bottom: 40px; font-size: 4rem; font-family: 'Great Vibes', cursive;">❤️ Your Favorite Things ❤️</h1>
            
            <div class="vinyl-record" onclick="togglePlay()">
                <div class="vinyl"></div>
            </div>
            
            <div class="song-title-enhanced">🎵 Coco Cola - Ruchika Jangid 🎵</div>
            
            <div class="audio-controls-enhanced">
                <button class="audio-btn-enhanced" onclick="playSong()">▶️ Play</button>
                <button class="audio-btn-enhanced" onclick="pauseSong()">⏸️ Pause</button>
                <button class="audio-btn-enhanced" onclick="restartSong()">🔄 Restart</button>
            </div>
            
            <audio id="song" loop>
    <source src="/static/coco_cola.mp3" type="audio/mpeg">
    Your browser does not support the audio element.
</audio>
            
            <div class="cute-quote-enhanced">
                "You're the melody in my life's song, the rhythm to my heart's beat. 
                Like your favorite song, our friendship is on repeat forever!" 
                <br><br>
                <span style="font-size: 1.5rem;">🎵 💕 🎵</span>
            </div>
        </div>
    </div>
    
    <!-- Birthday Wish -->
    <div id="wish" class="page">
        <div class="wish-container-enhanced">
            <h1 class="wish-title">Make a Birthday Wish ✨</h1>
            <p style="margin-bottom: 20px; color: #666; font-size: 1.2rem;">Close your eyes, make a wish, and type it here:</p>
            <textarea id="wishInput" class="wish-input-enhanced" rows="5" placeholder="Type your wish here..."></textarea>
            <br>
            <button class="wish-btn-enhanced" onclick="makeWish()">Send Wish to the Stars ✨</button>
            <div id="wishResponse" class="wish-message-enhanced"></div>
        </div>
    </div>
    
    <!-- Footer -->
    <div class="footer-enhanced">
        Made with infinite ❤️ especially for you, Mysha<br>
        <span style="font-size: 1rem;">Your birthday = The day the world became more beautiful</span>
    </div>
    
    <!-- Image Enlargement Modal -->
    <div id="imageModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.9); z-index: 2000; justify-content: center; align-items: center; cursor: pointer;" onclick="closeModal()">
        <img id="enlargedImage" style="max-width: 90%; max-height: 90%; border-radius: 20px; box-shadow: 0 0 50px gold;">
    </div>
    
    <script>
        // Game variables
        let gameScore = 0;
        let gameAttempts = 0;
        let achievements = {
            novice: false,
            master: false,
            legend: false
        };
        
        // Initialize particles
        function createParticles() {
            const particlesContainer = document.getElementById('particles');
            for (let i = 0; i < 50; i++) {
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.left = Math.random() * 100 + '%';
                particle.style.width = Math.random() * 10 + 5 + 'px';
                particle.style.height = particle.style.width;
                particle.style.animationDuration = Math.random() * 10 + 10 + 's';
                particle.style.animationDelay = Math.random() * 10 + 's';
                particle.style.background = `rgba(${Math.random() * 100 + 155}, ${Math.random() * 100 + 155}, 255, ${Math.random() * 0.5 + 0.3})`;
                particlesContainer.appendChild(particle);
            }
        }
        
        // Create floating hearts
        function createFloatingHearts() {
            const heartsContainer = document.getElementById('floatingHearts');
            for (let i = 0; i < 20; i++) {
                const heart = document.createElement('div');
                heart.className = 'heart';
                heart.innerHTML = ['❤️', '💕', '💗', '💓', '💖', '💘', '💝'][Math.floor(Math.random() * 7)];
                heart.style.left = Math.random() * 100 + '%';
                heart.style.animationDuration = Math.random() * 5 + 5 + 's';
                heart.style.animationDelay = Math.random() * 5 + 's';
                heart.style.fontSize = Math.random() * 30 + 20 + 'px';
                heartsContainer.appendChild(heart);
            }
        }
        
        // Hide loader after page load
        window.addEventListener('load', function() {
            setTimeout(() => {
                document.getElementById('loader').style.opacity = '0';
                setTimeout(() => {
                    document.getElementById('loader').style.display = 'none';
                }, 1000);
            }, 2000);
            
            createParticles();
            createFloatingHearts();
        });
        
        function showPage(pageId) {
            // Hide all pages with animation
            document.querySelectorAll('.page').forEach(page => {
                page.classList.remove('active');
            });
            
            // Show selected page
            document.getElementById(pageId).classList.add('active');
            
            // Scroll to top
            window.scrollTo({ top: 0, behavior: 'smooth' });
            
            // Add page transition sound effect (conceptual)
            playSoundEffect('pageFlip');
        }
        
        function startDrama() {
            showPage('memory');
            createConfetti(100);
            playSoundEffect('drama');
        }

        function showSecretMessage() {
    // Locked box ko hide karo
    document.getElementById('lockedBox').style.display = 'none';
    
    // Emotional message dikhao
    document.getElementById('emotional-message').style.display = 'block';
    
    // Confetti daalo
    createConfetti(100);
    
    // Sound effect (optional)
    playSoundEffect('unlock');
}
        
        function unlockSecret() {
            const now = new Date();
            const targetDate = new Date('2026-02-19T00:00:00');
            
            // For testing, you can remove this condition
            if (now >= targetDate) {
                document.querySelector('.locked-message').style.display = 'none';
                document.getElementById('emotional-message').style.display = 'block';
                createConfetti(50);
                playSoundEffect('unlock');
            } else {
                // Show time remaining
                const diff = targetDate - now;
                const hours = Math.floor(diff / (1000 * 60 * 60));
                const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
                
                // Custom alert
                showCustomAlert(`⏰ This message will unlock on Feb 19, 2026 at 12:00 AM!\\n\\nTime remaining: ${hours} hours and ${minutes} minutes`);
            }
        }
        
        function playGame() {
            gameAttempts++;
            let random = Math.random();
            
            // Animation on click
            const jetha = document.querySelector('.jethalal-3d');
            jetha.style.transform = 'scale(0.9) rotate(5deg)';
            setTimeout(() => {
                jetha.style.transform = '';
            }, 200);
            
            if (random < 0.4) { // 40% chance to find Gada
                gameScore += 10;
                
                // Check achievements
                if (gameScore >= 50 && !achievements.novice) {
                    achievements.novice = true;
                    document.getElementById('achievement1').style.opacity = '1';
                    showCustomAlert('🏆 Achievement Unlocked: Novice Gada Finder!');
                }
                if (gameScore >= 100 && !achievements.master) {
                    achievements.master = true;
                    document.getElementById('achievement2').style.opacity = '1';
                    showCustomAlert('🏆 Achievement Unlocked: Gada Master!');
                }
                if (gameScore >= 200 && !achievements.legend) {
                    achievements.legend = true;
                    document.getElementById('achievement3').style.opacity = '1';
                    showCustomAlert('🏆 Achievement Unlocked: LEGEND! You\\'re the Gada Queen!');
                }
                
                document.getElementById('score').innerHTML = `Score: ${gameScore}`;
                document.getElementById('attempts').innerHTML = `Attempts: ${gameAttempts}`;
                document.getElementById('gameMessage').innerHTML = '🎉 YAY! You found Gada! +10 points! 🎉';
                createConfetti(30);
                playSoundEffect('success');
                
                // Make Jethalal happy
                document.querySelector('.mouth').style.transform = 'scaleX(1.2)';
                setTimeout(() => {
                    document.querySelector('.mouth').style.transform = '';
                }, 500);
            } else {
                document.getElementById('gameMessage').innerHTML = '😅 Tapdhili! Try again, Jethalal needs you!';
                document.getElementById('attempts').innerHTML = `Attempts: ${gameAttempts}`;
                playSoundEffect('fail');
                
                // Make Jethalal sad
                document.querySelector('.mouth').style.transform = 'scaleY(0.5)';
                setTimeout(() => {
                    document.querySelector('.mouth').style.transform = '';
                }, 500);
            }
        }
        
        function resetGame() {
            gameScore = 0;
            gameAttempts = 0;
            achievements = { novice: false, master: false, legend: false };
            
            document.getElementById('score').innerHTML = 'Score: 0';
            document.getElementById('attempts').innerHTML = 'Attempts: 0';
            document.getElementById('gameMessage').innerHTML = '';
            document.getElementById('achievement1').style.opacity = '0.3';
            document.getElementById('achievement2').style.opacity = '0.3';
            document.getElementById('achievement3').style.opacity = '0.3';
            
            showCustomAlert('🔄 Game reset! Start fresh!');
        }
        
        function scratchGift() {
            const overlay = document.getElementById('scratchOverlay');
            overlay.style.opacity = '0';
            overlay.style.transform = 'scale(1.1)';
            
            setTimeout(() => {
                overlay.style.display = 'none';
                document.getElementById('giftContent').style.display = 'block';
                startCountdown();
                createConfetti(50);
                playSoundEffect('scratch');
            }, 800);
        }
        
        function startCountdown() {
            const birthday = new Date('2026-02-19T00:00:00');
            
            function updateCountdown() {
                const now = new Date();
                const diff = birthday - now;
                
                if (diff <= 0) {
                    document.getElementById('countdown').innerHTML = '🎁 YOUR GIFT IS READY! 🎁';
                    return;
                }
                
                const days = Math.floor(diff / (1000 * 60 * 60 * 24));
                const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
                const seconds = Math.floor((diff % (1000 * 60)) / 1000);
                
                document.getElementById('countdown').innerHTML = 
                    `⏰ Countdown to your real gift: ${days}d ${hours}h ${minutes}m ${seconds}s ⏰`;
            }
            
            updateCountdown();
            setInterval(updateCountdown, 1000);
        }
        
        function redeemCoupon(type) {
            const coupons = {
                hug: '🤗 Free Hug coupon activated! Come get your hug!',
                treat: '🍕 Free Treat coupon activated! Where should we go?',
                movie: '🎬 Movie Night coupon activated! What shall we watch?',
                shopping: '🛍️ Shopping Day coupon activated! Let\\'s hit the mall!'
            };
            
            showCustomAlert('🎟️ ' + coupons[type]);
            createConfetti(20);
            playSoundEffect('coupon');
        }
        
        let isPlaying = false;
        
        function playSong() {
            document.getElementById('song').play();
            isPlaying = true;
            document.querySelector('.vinyl-record').style.animationPlayState = 'running';
            playSoundEffect('play');
        }
        
        function pauseSong() {
            document.getElementById('song').pause();
            isPlaying = false;
            document.querySelector('.vinyl-record').style.animationPlayState = 'paused';
        }
        
        function restartSong() {
            document.getElementById('song').currentTime = 0;
            playSong();
        }
        
        function togglePlay() {
            if (isPlaying) {
                pauseSong();
            } else {
                playSong();
            }
        }
        
        function makeWish() {
            const wish = document.getElementById('wishInput').value;
            if (wish.trim() === '') {
                showCustomAlert('✨ Please type your wish first! ✨');
                return;
            }
            
            const response = document.getElementById('wishResponse');
            response.innerHTML = `
                ✨ Your wish has been sent to the stars! ✨<br><br>
                <span style="font-size: 1.5rem;">"${wish}"</span><br><br>
                May all your dreams come true! 🌟
            `;
            response.style.display = 'block';
            
            // Clear input
            document.getElementById('wishInput').value = '';
            
            createConfetti(50);
            playSoundEffect('wish');
        }
        
        function enlargeImage(card) {
            const img = card.querySelector('img').src;
            document.getElementById('enlargedImage').src = img;
            document.getElementById('imageModal').style.display = 'flex';
        }
        
        function closeModal() {
            document.getElementById('imageModal').style.display = 'none';
        }
        
        function createConfetti(count = 50) {
            for (let i = 0; i < count; i++) {
                setTimeout(() => {
                    const confetti = document.createElement('div');
                    confetti.style.position = 'fixed';
                    confetti.style.left = Math.random() * 100 + '%';
                    confetti.style.top = '-10px';
                    confetti.style.width = Math.random() * 15 + 5 + 'px';
                    confetti.style.height = confetti.style.width;
                    confetti.style.backgroundColor = `hsl(${Math.random() * 360}, 100%, 50%)`;
                    confetti.style.borderRadius = Math.random() > 0.5 ? '50%' : '0';
                    confetti.style.transform = `rotate(${Math.random() * 360}deg)`;
                    confetti.style.zIndex = '9999';
                    confetti.style.pointerEvents = 'none';
                    confetti.style.boxShadow = '0 0 10px rgba(255,255,255,0.5)';
                    
                    document.body.appendChild(confetti);
                    
                    let animation = confetti.animate([
                        { transform: `translateY(0) rotate(0deg)`, opacity: 1 },
                        { transform: `translateY(${window.innerHeight}px) rotate(${Math.random() * 720}deg)`, opacity: 0.8 }
                    ], {
                        duration: 2000 + Math.random() * 1000,
                        easing: 'cubic-bezier(0.25, 0.1, 0.25, 1)'
                    });
                    
                    animation.onfinish = () => confetti.remove();
                }, i * 30);
            }
        }
        
        function showCustomAlert(message) {
            // Create custom alert
            const alert = document.createElement('div');
            alert.style.position = 'fixed';
            alert.style.top = '50%';
            alert.style.left = '50%';
            alert.style.transform = 'translate(-50%, -50%) scale(0)';
            alert.style.background = 'linear-gradient(135deg, #667eea, #764ba2)';
            alert.style.color = 'white';
            alert.style.padding = '30px';
            alert.style.borderRadius = '20px';
            alert.style.boxShadow = '0 20px 40px rgba(0,0,0,0.3), 0 0 0 3px gold, 0 0 50px rgba(255,215,0,0.3)';
            alert.style.zIndex = '10000';
            alert.style.maxWidth = '400px';
            alert.style.textAlign = 'center';
            alert.style.fontSize = '1.2rem';
            alert.style.transition = 'transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
            alert.innerHTML = message.replace(/\\n/g, '<br>');
            
            document.body.appendChild(alert);
            
            // Animate in
            setTimeout(() => {
                alert.style.transform = 'translate(-50%, -50%) scale(1)';
            }, 10);
            
            // Remove after 3 seconds
            setTimeout(() => {
                alert.style.transform = 'translate(-50%, -50%) scale(0)';
                setTimeout(() => {
                    alert.remove();
                }, 300);
            }, 3000);
        }
        
        function playSoundEffect(type) {
            // This is a conceptual function - in a real app, you'd play actual sounds
            // For now, we'll just console.log
            console.log(`Playing sound effect: ${type}`);
        }
        
        // Keyboard navigation
        document.addEventListener('keydown', function(e) {
            if (e.key >= '1' && e.key <= '7') {
                const pages = ['home', 'memory', 'secret', 'video', 'gift', 'favorite', 'wish'];
                const index = parseInt(e.key) - 1;
                if (pages[index]) {
                    showPage(pages[index]);
                }
            }
        });
        
        // Initialize countdown if on gift page
        if (window.location.hash === '#gift') {
            startCountdown();
        }
        
        // Check if it's birthday
        function checkBirthday() {
            const today = new Date();
            if (today.getMonth() === 1 && today.getDate() === 19) {
                document.querySelectorAll('.nav-btn').forEach(btn => {
                    btn.style.background = 'linear-gradient(135deg, gold, orange)';
                });
            }
        }
        
        checkBirthday();
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/static/<path:filename>')
def serve_static(filename):
    try:
        return send_from_directory('static', filename)
    except:
        return "File not found", 404

# Special route for video
@app.route('/video')
def serve_video():
    try:
        return send_from_directory('static', 'vid1.mp4')
    except Exception as e:
        print(f"Video error: {e}")
        return "Video not found", 404

@app.route('/api/time-until-birthday')
def time_until_birthday():
    birthday = datetime(2026, 2, 19, 0, 0, 0)
    now = datetime.now()
    diff = birthday - now
    
    return jsonify({
        'days': diff.days,
        'hours': diff.seconds // 3600,
        'minutes': (diff.seconds % 3600) // 60,
        'seconds': diff.seconds % 60
    })

@app.route('/api/save-wish', methods=['POST'])
def save_wish():
    wish = request.json.get('wish', '')
    # In a real app, you might save this to a database
    return jsonify({'status': 'success', 'message': 'Wish saved!'})



if __name__ == '__main__':
    # Create static directory if it doesn't exist
    if not os.path.exists('static'):
        os.makedirs('static')
    
    # Instructions for adding media files
    print("\n" + "="*70)
    print("🎂 ENHANCED BIRTHDAY APP FOR MYSHA - THE QUEEN'S SPECIAL DAY 🎂")
    print("="*70)
    print("\n✨ PREMIUM FEATURES INCLUDED:")
    print("   • 3D animated cake with realistic flame")
    print("   • Floating particles and hearts background")
    print("   • 3D Jethalal game with achievements system")
    print("   • Vinyl record player animation")
    print("   • Scratch card with 3D flip effect")
    print("   • Custom alerts and notifications")
    print("   • Confetti explosions")
    print("   • Keyboard navigation (press 1-8)")
    print("   • Image enlargement modal")
    print("   • Achievement system")
    print("   • Loading animation")
    print("   • Responsive design")
    print("   • And much more...")
    
    print("\n📁 REQUIRED FILES (Place in 'static' folder):")
    print("   1. Video file: 'birthday_video.mp4' - Your personal message")
    print("   2. Audio file: 'coco_cola.mp3' - Her favorite song")
    print("\n   For photos: Replace placeholder URLs or add to static/ folder")
    
    print("\n🚀 READY TO LAUNCH!")
    print("   Run the app and open: http://127.0.0.1:5000")
    print("   OR: http://localhost:5000")
    print("\n💝 Test everything before Feb 19, 2026!")
    print("   The secret message will unlock exactly at midnight on her birthday")
    
    print("\n" + "="*70)
    print("🎉 HAPPY BIRTHDAY IN ADVANCE, MYSHA! 🎉")
    print("="*70)
    
    # Run with specific host and port, and disable debug mode initially
    app.run(debug=False, host='127.0.0.1', port=5000)