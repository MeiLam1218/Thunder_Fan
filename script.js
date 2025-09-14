// Lightning Stroke Visualization for Hong Kong Territory
class LightningVisualization {
    constructor() {
        this.canvas = document.getElementById('lightningCanvas');
        this.ctx = this.canvas.getContext('2d');
        this.setupCanvas();
        
        // Animation state
        this.isPlaying = false;
        this.currentMonthIndex = 0;
        this.animationSpeed = 1;
        this.lastFrameTime = 0;
        this.monthDuration = 2000; // 2 seconds per month
        
        // Lightning particles
        this.lightningBolts = [];
        this.particles = [];
        
        // Monthly lightning stroke data for Hong Kong (sample data)
        this.lightningData = [
            { month: 'January', strokes: 23, intensity: 'low' },
            { month: 'February', strokes: 18, intensity: 'low' },
            { month: 'March', strokes: 45, intensity: 'low' },
            { month: 'April', strokes: 89, intensity: 'medium' },
            { month: 'May', strokes: 156, intensity: 'medium' },
            { month: 'June', strokes: 298, intensity: 'high' },
            { month: 'July', strokes: 445, intensity: 'high' },
            { month: 'August', strokes: 387, intensity: 'high' },
            { month: 'September', strokes: 234, intensity: 'high' },
            { month: 'October', strokes: 123, intensity: 'medium' },
            { month: 'November', strokes: 67, intensity: 'medium' },
            { month: 'December', strokes: 34, intensity: 'low' }
        ];
        
        this.setupEventListeners();
        this.updateUI();
        this.animate();
    }
    
    setupCanvas() {
        this.canvas.width = 800;
        this.canvas.height = 600;
    }
    
    setupEventListeners() {
        document.getElementById('playBtn').addEventListener('click', () => this.play());
        document.getElementById('pauseBtn').addEventListener('click', () => this.pause());
        document.getElementById('resetBtn').addEventListener('click', () => this.reset());
        
        const speedSlider = document.getElementById('speed');
        speedSlider.addEventListener('input', (e) => {
            this.animationSpeed = parseFloat(e.target.value);
            document.getElementById('speedValue').textContent = `${this.animationSpeed}x`;
        });
    }
    
    play() {
        this.isPlaying = true;
    }
    
    pause() {
        this.isPlaying = false;
    }
    
    reset() {
        this.isPlaying = false;
        this.currentMonthIndex = 0;
        this.lightningBolts = [];
        this.particles = [];
        this.updateUI();
        this.clearCanvas();
    }
    
    updateUI() {
        const currentData = this.lightningData[this.currentMonthIndex];
        document.getElementById('currentMonth').textContent = `Month: ${currentData.month}`;
        document.getElementById('strokeCount').textContent = `Strokes: ${currentData.strokes}`;
        document.getElementById('intensity').textContent = `Intensity: ${currentData.intensity.charAt(0).toUpperCase() + currentData.intensity.slice(1)}`;
    }
    
    clearCanvas() {
        this.ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
    }
    
    getIntensityColor(intensity) {
        switch(intensity) {
            case 'low': return '#ffff00';
            case 'medium': return '#ff8800';
            case 'high': return '#ff0000';
            default: return '#ffffff';
        }
    }
    
    createLightningBolt(startX, startY, intensity) {
        const bolt = {
            segments: [],
            color: this.getIntensityColor(intensity),
            opacity: 1,
            life: 20,
            maxLife: 20
        };
        
        // Generate jagged lightning path
        let currentX = startX;
        let currentY = startY;
        const targetY = this.canvas.height;
        const segmentLength = 20;
        
        while (currentY < targetY) {
            const nextX = currentX + (Math.random() - 0.5) * 40;
            const nextY = currentY + segmentLength + Math.random() * 20;
            
            bolt.segments.push({
                x1: currentX,
                y1: currentY,
                x2: nextX,
                y2: nextY
            });
            
            currentX = nextX;
            currentY = nextY;
        }
        
        return bolt;
    }
    
    createParticle(x, y, color) {
        return {
            x: x,
            y: y,
            vx: (Math.random() - 0.5) * 4,
            vy: (Math.random() - 0.5) * 4,
            color: color,
            opacity: 1,
            life: 30,
            maxLife: 30,
            size: Math.random() * 3 + 1
        };
    }
    
    generateLightning() {
        const currentData = this.lightningData[this.currentMonthIndex];
        const probability = Math.min(currentData.strokes / 500, 0.8); // Max 80% chance
        
        if (Math.random() < probability * this.animationSpeed) {
            const startX = Math.random() * this.canvas.width;
            const startY = 0;
            const bolt = this.createLightningBolt(startX, startY, currentData.intensity);
            this.lightningBolts.push(bolt);
            
            // Create particles at strike point
            for (let i = 0; i < 10; i++) {
                const particle = this.createParticle(startX, startY, bolt.color);
                this.particles.push(particle);
            }
            
            // Flash effect
            this.canvas.classList.add('lightning-flash');
            setTimeout(() => {
                this.canvas.classList.remove('lightning-flash');
            }, 200);
        }
    }
    
    updateLightning() {
        // Update lightning bolts
        this.lightningBolts = this.lightningBolts.filter(bolt => {
            bolt.life--;
            bolt.opacity = bolt.life / bolt.maxLife;
            return bolt.life > 0;
        });
        
        // Update particles
        this.particles = this.particles.filter(particle => {
            particle.x += particle.vx;
            particle.y += particle.vy;
            particle.vx *= 0.98;
            particle.vy *= 0.98;
            particle.life--;
            particle.opacity = particle.life / particle.maxLife;
            return particle.life > 0;
        });
    }
    
    drawLightning() {
        // Draw lightning bolts
        this.lightningBolts.forEach(bolt => {
            this.ctx.strokeStyle = bolt.color;
            this.ctx.globalAlpha = bolt.opacity;
            this.ctx.lineWidth = 3;
            this.ctx.lineCap = 'round';
            
            // Draw main bolt
            this.ctx.beginPath();
            bolt.segments.forEach((segment, index) => {
                if (index === 0) {
                    this.ctx.moveTo(segment.x1, segment.y1);
                }
                this.ctx.lineTo(segment.x2, segment.y2);
            });
            this.ctx.stroke();
            
            // Draw glow effect
            this.ctx.strokeStyle = bolt.color;
            this.ctx.globalAlpha = bolt.opacity * 0.3;
            this.ctx.lineWidth = 8;
            this.ctx.beginPath();
            bolt.segments.forEach((segment, index) => {
                if (index === 0) {
                    this.ctx.moveTo(segment.x1, segment.y1);
                }
                this.ctx.lineTo(segment.x2, segment.y2);
            });
            this.ctx.stroke();
        });
        
        // Draw particles
        this.particles.forEach(particle => {
            this.ctx.fillStyle = particle.color;
            this.ctx.globalAlpha = particle.opacity;
            this.ctx.beginPath();
            this.ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
            this.ctx.fill();
        });
        
        this.ctx.globalAlpha = 1;
    }
    
    drawBackground() {
        // Create animated background
        const gradient = this.ctx.createRadialGradient(
            this.canvas.width / 2, this.canvas.height / 2, 0,
            this.canvas.width / 2, this.canvas.height / 2, this.canvas.width / 2
        );
        
        gradient.addColorStop(0, 'rgba(10, 10, 10, 0.9)');
        gradient.addColorStop(1, 'rgba(0, 0, 0, 0.95)');
        
        this.ctx.fillStyle = gradient;
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Draw Hong Kong outline (simplified)
        this.drawHongKongOutline();
    }
    
    drawHongKongOutline() {
        this.ctx.strokeStyle = 'rgba(0, 245, 255, 0.3)';
        this.ctx.lineWidth = 2;
        this.ctx.setLineDash([5, 5]);
        
        // Simplified Hong Kong territory outline
        this.ctx.beginPath();
        this.ctx.rect(this.canvas.width * 0.2, this.canvas.height * 0.3, 
                     this.canvas.width * 0.6, this.canvas.height * 0.4);
        this.ctx.stroke();
        
        this.ctx.setLineDash([]);
        
        // Add location label
        this.ctx.fillStyle = 'rgba(0, 245, 255, 0.6)';
        this.ctx.font = '14px Arial';
        this.ctx.textAlign = 'center';
        this.ctx.fillText('Hong Kong Territory', this.canvas.width / 2, this.canvas.height * 0.25);
    }
    
    animate(currentTime = 0) {
        const deltaTime = currentTime - this.lastFrameTime;
        
        if (this.isPlaying && deltaTime > this.monthDuration / this.animationSpeed) {
            this.currentMonthIndex = (this.currentMonthIndex + 1) % this.lightningData.length;
            this.updateUI();
            this.lastFrameTime = currentTime;
        }
        
        this.drawBackground();
        
        if (this.isPlaying) {
            this.generateLightning();
        }
        
        this.updateLightning();
        this.drawLightning();
        
        requestAnimationFrame((time) => this.animate(time));
    }
}

// Initialize the visualization when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new LightningVisualization();
});