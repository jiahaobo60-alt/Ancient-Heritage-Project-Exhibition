import * as THREE from "three";
import { OrbitControls } from "../gallery-master/node_modules/three/examples/jsm/controls/OrbitControls.js";

const container = document.getElementById("museumCanvas");
const panelTitle = document.getElementById("panelTitle");
const panelMeta = document.getElementById("panelMeta");
const panelDesc = document.getElementById("panelDesc");
const panelTag = document.getElementById("panelTag");
const panelDetails = document.getElementById("panelDetails");
const viewButtons = document.querySelectorAll(".view-btn");

const exhibits = [
    {
        id: "yingxian",
        name: "应县木塔",
        meta: "辽代 · 山西应县 · 木构塔式建筑",
        image: "img/应县木塔-辽代-山西应县/yingxian_01.jpg",
        accent: 0xB48A5A,
        position: new THREE.Vector3(-8.5, 1.8, -5.4),
        rotationY: Math.PI * 0.12,
        desc: "世界现存最高、最古老的木构塔式建筑，以纯木构架和多样斗拱体系展现辽代营造智慧。",
        details: [
            ["年代", "辽清宁二年"],
            ["高度", "67.31米"],
            ["结构", "楼阁式木塔"],
            ["看点", "斗拱与榫卯"]
        ]
    },
    {
        id: "foguang",
        name: "佛光寺东大殿",
        meta: "唐代 · 山西五台山 · 庑殿顶佛殿",
        image: "img/佛光寺东大殿-唐代-山西五台山/foguang_01.jpg",
        accent: 0x8B6F47,
        position: new THREE.Vector3(8.5, 1.8, -5.4),
        rotationY: -Math.PI * 0.12,
        desc: "中国现存重要唐代木构建筑，屋身比例舒展、斗拱雄大，体现唐代建筑的开阔气象。",
        details: [
            ["年代", "唐大中十一年"],
            ["地点", "山西五台"],
            ["屋顶", "单檐庑殿顶"],
            ["看点", "唐代斗拱"]
        ]
    },
    {
        id: "taihe",
        name: "太和殿",
        meta: "明清 · 北京故宫 · 皇家宫殿",
        image: "img/太和殿-明清-北京故宫/taihe_01.jpg",
        accent: 0xB7372D,
        position: new THREE.Vector3(-8.5, 1.8, 5.6),
        rotationY: Math.PI * 0.88,
        desc: "紫禁城核心大殿，重檐庑殿顶与高台基共同构成皇家建筑最具礼制感的空间秩序。",
        details: [
            ["年代", "明清"],
            ["地点", "北京故宫"],
            ["等级", "重檐庑殿顶"],
            ["看点", "礼制轴线"]
        ]
    },
    {
        id: "zhuozheng",
        name: "拙政园",
        meta: "明代 · 江苏苏州 · 江南园林",
        image: "img/拙政园-明代-江苏苏州/zhuozheng_01.jpg",
        accent: 0x4F7D59,
        position: new THREE.Vector3(8.5, 1.8, 5.6),
        rotationY: -Math.PI * 0.88,
        desc: "江南私家园林代表，以水为中心组织亭台楼阁、曲桥与借景，呈现可行、可望、可游的园林体验。",
        details: [
            ["年代", "明代"],
            ["地点", "江苏苏州"],
            ["类型", "私家园林"],
            ["看点", "水院与借景"]
        ]
    }
];

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x171D27);
scene.fog = new THREE.Fog(0x171D27, 20, 48);

const camera = new THREE.PerspectiveCamera(58, 1, 0.1, 120);
camera.position.set(0, 11.5, 14);

const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
container.appendChild(renderer.domElement);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.08;
controls.enablePan = false;
controls.minDistance = 4;
controls.maxDistance = 24;
controls.maxPolarAngle = Math.PI * 0.54;
controls.target.set(0, 0.4, 0);

const textureLoader = new THREE.TextureLoader();
const raycaster = new THREE.Raycaster();
const pointer = new THREE.Vector2();
const clock = new THREE.Clock();
const pressed = new Set();
const interactive = [];
let selected = exhibits[0];
let focusIndex = 0;

init();
animate();

function init() {
    addLights();
    addHall();
    addExhibits();
    addBuildingModels();
    addEvents();
    resize();
    updatePanel(selected);
}

function addLights() {
    scene.add(new THREE.HemisphereLight(0xF8E6C0, 0x27384A, 1.8));

    const key = new THREE.DirectionalLight(0xFFF4D4, 2.6);
    key.position.set(5, 12, 7);
    key.castShadow = true;
    key.shadow.mapSize.set(2048, 2048);
    key.shadow.camera.left = -18;
    key.shadow.camera.right = 18;
    key.shadow.camera.top = 18;
    key.shadow.camera.bottom = -18;
    scene.add(key);

    const warmSpots = [
        [-8, 6, -5],
        [8, 6, -5],
        [-8, 6, 5],
        [8, 6, 5]
    ];

    warmSpots.forEach(([x, y, z]) => {
        const lamp = new THREE.PointLight(0xFFDCA5, 1.4, 13);
        lamp.position.set(x, y, z);
        scene.add(lamp);
    });

    const center = new THREE.SpotLight(0xFFE3B0, 4.2, 26, Math.PI * 0.28, 0.45, 1.1);
    center.position.set(0, 9, 8);
    center.target.position.set(0, 0.8, 0);
    center.castShadow = true;
    scene.add(center);
    scene.add(center.target);
}

function addHall() {
    const floor = new THREE.Mesh(
        new THREE.PlaneGeometry(28, 24),
        new THREE.MeshStandardMaterial({
            color: 0x2A3241,
            roughness: 0.62,
            metalness: 0.08
        })
    );
    floor.rotation.x = -Math.PI / 2;
    floor.receiveShadow = true;
    scene.add(floor);

    const grid = new THREE.GridHelper(28, 28, 0xA29192, 0x50596C);
    grid.position.y = 0.012;
    grid.material.opacity = 0.22;
    grid.material.transparent = true;
    scene.add(grid);

    const wallMat = new THREE.MeshStandardMaterial({
        color: 0x202735,
        roughness: 0.72
    });
    addWall(0, 3, -12, 28, 6, 0.32, wallMat);
    addWall(0, 3, 12, 28, 6, 0.32, wallMat);
    addWall(-14, 3, 0, 0.32, 6, 24, wallMat);
    addWall(14, 3, 0, 0.32, 6, 24, wallMat);

    const roofMat = new THREE.MeshStandardMaterial({ color: 0x3F2630, roughness: 0.68 });
    for (let z = -10; z <= 10; z += 4) {
        const beam = new THREE.Mesh(new THREE.BoxGeometry(28, 0.28, 0.34), roofMat);
        beam.position.set(0, 5.95, z);
        beam.castShadow = true;
        scene.add(beam);
    }
    for (let x = -12; x <= 12; x += 4) {
        const beam = new THREE.Mesh(new THREE.BoxGeometry(0.28, 0.34, 24), roofMat);
        beam.position.set(x, 5.72, 0);
        beam.castShadow = true;
        scene.add(beam);
    }

    const columnMat = new THREE.MeshStandardMaterial({ color: 0x7D2F2A, roughness: 0.5 });
    [-11.8, 11.8].forEach((x) => {
        [-9.5, -3.2, 3.2, 9.5].forEach((z) => {
            const column = new THREE.Mesh(new THREE.CylinderGeometry(0.22, 0.28, 5.6, 24), columnMat);
            column.position.set(x, 2.8, z);
            column.castShadow = true;
            column.receiveShadow = true;
            scene.add(column);
        });
    });

    const pool = new THREE.Mesh(
        new THREE.PlaneGeometry(6.2, 2.4),
        new THREE.MeshStandardMaterial({
            color: 0x29566B,
            roughness: 0.18,
            metalness: 0.18,
            transparent: true,
            opacity: 0.82
        })
    );
    pool.rotation.x = -Math.PI / 2;
    pool.position.y = 0.025;
    scene.add(pool);

    const stage = new THREE.Mesh(
        new THREE.CylinderGeometry(5.8, 6.2, 0.32, 64),
        new THREE.MeshStandardMaterial({ color: 0x3B4353, roughness: 0.48, metalness: 0.08 })
    );
    stage.position.y = 0.16;
    stage.castShadow = true;
    stage.receiveShadow = true;
    scene.add(stage);

    const ring = new THREE.Mesh(
        new THREE.TorusGeometry(6.05, 0.045, 12, 96),
        new THREE.MeshStandardMaterial({ color: 0xD4A574, emissive: 0x3B2610, roughness: 0.35 })
    );
    ring.rotation.x = Math.PI / 2;
    ring.position.y = 0.36;
    scene.add(ring);
}

function addWall(x, y, z, width, height, depth, material) {
    const wall = new THREE.Mesh(new THREE.BoxGeometry(width, height, depth), material);
    wall.position.set(x, y, z);
    wall.receiveShadow = true;
    scene.add(wall);
}

function addExhibits() {
    exhibits.forEach((item) => {
        const group = new THREE.Group();
        group.position.copy(item.position);
        group.rotation.y = item.rotationY;

        const frame = new THREE.Mesh(
            new THREE.BoxGeometry(4.25, 3.05, 0.16),
            new THREE.MeshStandardMaterial({ color: item.accent, roughness: 0.48 })
        );
        frame.castShadow = true;
        frame.receiveShadow = true;
        group.add(frame);

        const imageMat = new THREE.MeshStandardMaterial({
            color: 0xFFFFFF,
            roughness: 0.45,
            map: textureLoader.load(item.image, (texture) => {
                texture.colorSpace = THREE.SRGBColorSpace;
                texture.anisotropy = 8;
            })
        });
        const image = new THREE.Mesh(new THREE.PlaneGeometry(3.75, 2.42), imageMat);
        image.position.z = 0.09;
        image.userData.exhibit = item;
        group.add(image);
        interactive.push(image);

        const label = makeTextSprite(item.name, item.meta, item.accent);
        label.position.set(0, -2.0, 0.18);
        group.add(label);

        const pedestal = new THREE.Mesh(
            new THREE.BoxGeometry(4.8, 0.18, 0.72),
            new THREE.MeshStandardMaterial({ color: 0xA29192, roughness: 0.54 })
        );
        pedestal.position.set(0, -1.72, 0);
        pedestal.castShadow = true;
        group.add(pedestal);

        scene.add(group);
    });
}

function addBuildingModels() {
    createTower(-3.25, -1.9, 0xB48A5A);
    createHall(3.25, -1.9, 0x8B6F47);
    createPalace(-3.25, 2.25, 0xB7372D);
    createGarden(3.25, 2.25, 0x4F7D59);
}

function createTower(x, z, color) {
    const group = new THREE.Group();
    group.position.set(x, 0, z);
    group.scale.setScalar(1.22);
    const mat = new THREE.MeshStandardMaterial({ color, roughness: 0.52 });
    for (let i = 0; i < 6; i += 1) {
        const body = new THREE.Mesh(new THREE.CylinderGeometry(0.75 - i * 0.07, 0.86 - i * 0.07, 0.5, 8), mat);
        body.position.y = 0.28 + i * 0.55;
        body.castShadow = true;
        group.add(body);
        const eave = new THREE.Mesh(new THREE.CylinderGeometry(1.05 - i * 0.08, 0.94 - i * 0.08, 0.08, 8), mat);
        eave.position.y = 0.55 + i * 0.55;
        eave.castShadow = true;
        group.add(eave);
    }
    scene.add(group);
}

function createHall(x, z, color) {
    const group = new THREE.Group();
    group.position.set(x, 0, z);
    group.scale.setScalar(1.28);
    const body = new THREE.Mesh(new THREE.BoxGeometry(2.6, 0.9, 1.45), new THREE.MeshStandardMaterial({ color: 0x6F4634, roughness: 0.56 }));
    body.position.y = 0.55;
    body.castShadow = true;
    group.add(body);
    const roof = new THREE.Mesh(new THREE.ConeGeometry(1.85, 0.62, 4), new THREE.MeshStandardMaterial({ color, roughness: 0.5 }));
    roof.scale.z = 0.72;
    roof.rotation.y = Math.PI / 4;
    roof.position.y = 1.28;
    roof.castShadow = true;
    group.add(roof);
    scene.add(group);
}

function createPalace(x, z, color) {
    const group = new THREE.Group();
    group.position.set(x, 0, z);
    group.scale.setScalar(1.24);
    const base = new THREE.Mesh(new THREE.BoxGeometry(3.1, 0.32, 1.9), new THREE.MeshStandardMaterial({ color: 0xC8B389, roughness: 0.5 }));
    base.position.y = 0.16;
    group.add(base);
    const body = new THREE.Mesh(new THREE.BoxGeometry(2.55, 0.9, 1.36), new THREE.MeshStandardMaterial({ color: 0x7D2F2A, roughness: 0.58 }));
    body.position.y = 0.78;
    body.castShadow = true;
    group.add(body);
    const roof = new THREE.Mesh(new THREE.BoxGeometry(3.15, 0.28, 1.88), new THREE.MeshStandardMaterial({ color, roughness: 0.48 }));
    roof.position.y = 1.38;
    roof.castShadow = true;
    group.add(roof);
    scene.add(group);
}

function createGarden(x, z, color) {
    const group = new THREE.Group();
    group.position.set(x, 0, z);
    group.scale.setScalar(1.32);
    const water = new THREE.Mesh(new THREE.CircleGeometry(1.3, 40), new THREE.MeshStandardMaterial({ color: 0x2F6E78, roughness: 0.22, metalness: 0.1 }));
    water.rotation.x = -Math.PI / 2;
    water.position.y = 0.04;
    group.add(water);
    const pavilion = new THREE.Mesh(new THREE.CylinderGeometry(0.48, 0.54, 0.75, 6), new THREE.MeshStandardMaterial({ color: 0x6F4634, roughness: 0.55 }));
    pavilion.position.set(0.1, 0.45, 0);
    pavilion.castShadow = true;
    group.add(pavilion);
    const roof = new THREE.Mesh(new THREE.ConeGeometry(0.72, 0.42, 6), new THREE.MeshStandardMaterial({ color, roughness: 0.46 }));
    roof.position.set(0.1, 1.05, 0);
    roof.castShadow = true;
    group.add(roof);
    scene.add(group);
}

function makeTextSprite(title, subtitle, accent) {
    const canvas = document.createElement("canvas");
    canvas.width = 1024;
    canvas.height = 256;
    const ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "rgba(24, 29, 39, 0.86)";
    roundRect(ctx, 48, 32, 928, 176, 24);
    ctx.fill();
    ctx.strokeStyle = `#${accent.toString(16).padStart(6, "0")}`;
    ctx.lineWidth = 5;
    ctx.stroke();
    ctx.fillStyle = "#FFF7DF";
    ctx.font = "700 54px SimSun, serif";
    ctx.fillText(title, 92, 108);
    ctx.fillStyle = "rgba(245, 241, 232, 0.78)";
    ctx.font = "34px SimSun, serif";
    ctx.fillText(subtitle, 92, 162);

    const texture = new THREE.CanvasTexture(canvas);
    texture.colorSpace = THREE.SRGBColorSpace;
    const sprite = new THREE.Sprite(new THREE.SpriteMaterial({ map: texture, transparent: true }));
    sprite.scale.set(3.2, 0.8, 1);
    return sprite;
}

function roundRect(ctx, x, y, width, height, radius) {
    ctx.beginPath();
    ctx.moveTo(x + radius, y);
    ctx.lineTo(x + width - radius, y);
    ctx.quadraticCurveTo(x + width, y, x + width, y + radius);
    ctx.lineTo(x + width, y + height - radius);
    ctx.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
    ctx.lineTo(x + radius, y + height);
    ctx.quadraticCurveTo(x, y + height, x, y + height - radius);
    ctx.lineTo(x, y + radius);
    ctx.quadraticCurveTo(x, y, x + radius, y);
    ctx.closePath();
}

function addEvents() {
    window.addEventListener("resize", resize);
    window.addEventListener("keydown", (event) => pressed.add(event.code));
    window.addEventListener("keyup", (event) => pressed.delete(event.code));
    renderer.domElement.addEventListener("click", handleClick);

    viewButtons.forEach((button) => {
        button.addEventListener("click", () => {
            viewButtons.forEach((item) => item.classList.remove("active"));
            button.classList.add("active");
            setView(button.dataset.view);
        });
    });
}

function handleClick(event) {
    const rect = renderer.domElement.getBoundingClientRect();
    pointer.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
    pointer.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;
    raycaster.setFromCamera(pointer, camera);
    const hit = raycaster.intersectObjects(interactive, false)[0];
    if (!hit) return;
    selected = hit.object.userData.exhibit;
    focusIndex = exhibits.findIndex((item) => item.id === selected.id);
    updatePanel(selected);
    focusExhibit(selected);
}

function updatePanel(item) {
    panelTag.textContent = "当前展品";
    panelTitle.textContent = item.name;
    panelMeta.textContent = item.meta;
    panelDesc.textContent = item.desc;
    panelDetails.innerHTML = item.details
        .map(([label, value]) => `<div class="panel-detail"><strong>${label}</strong><span>${value}</span></div>`)
        .join("");
}

function setView(view) {
    if (view === "center") {
        moveCamera(new THREE.Vector3(0, 4.1, 12.6), new THREE.Vector3(0, 1.8, 0));
    } else if (view === "overlook") {
        moveCamera(new THREE.Vector3(0, 15.5, 0.2), new THREE.Vector3(0, 0.6, 0));
    } else if (view === "focus") {
        focusIndex = (focusIndex + 1) % exhibits.length;
        selected = exhibits[focusIndex];
        updatePanel(selected);
        focusExhibit(selected);
    } else {
        moveCamera(new THREE.Vector3(0, 11.5, 14), new THREE.Vector3(0, 0.4, 0));
    }
}

function focusExhibit(item) {
    const direction = new THREE.Vector3(0, 0.35, 4.6).applyAxisAngle(new THREE.Vector3(0, 1, 0), item.rotationY);
    moveCamera(item.position.clone().add(direction), item.position.clone().add(new THREE.Vector3(0, 0.05, 0)));
}

function moveCamera(position, target) {
    camera.position.copy(position);
    controls.target.copy(target);
    controls.update();
}

function handleMovement(delta) {
    const speed = 5.5 * delta;
    const forward = new THREE.Vector3();
    camera.getWorldDirection(forward);
    forward.y = 0;
    forward.normalize();
    const right = new THREE.Vector3().crossVectors(forward, camera.up).normalize();
    const movement = new THREE.Vector3();

    if (pressed.has("KeyW") || pressed.has("ArrowUp")) movement.add(forward);
    if (pressed.has("KeyS") || pressed.has("ArrowDown")) movement.sub(forward);
    if (pressed.has("KeyA") || pressed.has("ArrowLeft")) movement.sub(right);
    if (pressed.has("KeyD") || pressed.has("ArrowRight")) movement.add(right);

    if (movement.lengthSq() === 0) return;
    movement.normalize().multiplyScalar(speed);

    const nextPosition = camera.position.clone().add(movement);
    nextPosition.x = THREE.MathUtils.clamp(nextPosition.x, -11.8, 11.8);
    nextPosition.z = THREE.MathUtils.clamp(nextPosition.z, -9.7, 9.7);
    nextPosition.y = THREE.MathUtils.clamp(nextPosition.y, 1.8, 15.5);
    const applied = nextPosition.sub(camera.position);
    camera.position.add(applied);
    controls.target.add(applied);
}

function resize() {
    const { clientWidth, clientHeight } = container;
    camera.aspect = clientWidth / Math.max(clientHeight, 1);
    camera.updateProjectionMatrix();
    renderer.setSize(clientWidth, clientHeight, false);
}

function animate() {
    const delta = Math.min(clock.getDelta(), 0.05);
    handleMovement(delta);
    controls.update();
    renderer.render(scene, camera);
    requestAnimationFrame(animate);
}
