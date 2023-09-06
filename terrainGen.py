from ursina import *
from perlin_noise import PerlinNoise
from ursina.shaders import basic_lighting_shader
from ursina.prefabs.first_person_controller import FirstPersonController
from threading import Thread

def scale(val, src, dst):
    """
    Scale the given value from the scale of src to the scale of dst.
    """
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]


noise = PerlinNoise(1,100)

class TerrainChunk(Entity):
    def __init__(self,offset,**kwargs):
        self.xSize = 5
        self.zSise = 5
        self.height = 0
        self.depth = 0
        self.offset = offset
        self.type = 'terrain'
        self.cellSize = 20
        self.vertexOffset = self.xSize * 0.5

        self.vertices = []
        self.triangles = []
        self.uvs = []
        self.colors = []
        self.generate_terrain()
        super().__init__(
            model = Mesh(vertices=self.vertices,triangles=self.triangles,uvs=self.uvs,colors=self.colors),
            position=offset,
            **kwargs
        )
        self.model.generate_normals(False)
        self.model.colors = self.colors

    def generate_terrain(self):
        vertex = 0
        for z in range(self.zSise+1):
            for x in range(self.xSize+1):
                X = (x*self.cellSize)-self.vertexOffset
                Z = (z*self.cellSize)-self.vertexOffset
                y = noise(((X+self.offset[0])*0.02,(Z+self.offset[2])*0.02)) * 7

                if y > self.height:
                    self.height = y
                if y < self.depth:
                    self.depth = y

                self.vertices.append(Vec3(X,y,Z))
                self.uvs.append(Vec2(x/self.xSize,z/self.zSise))

                if x < self.xSize and z < self.zSise:
                    self.triangles.extend([vertex+0,vertex+1,vertex+self.xSize+2,vertex+0,vertex+self.xSize+2,vertex+self.xSize+1])
                    vertex += 1
            if x <= self.xSize and z <= self.zSise:
                vertex += 1

def load_chunks(current):
    if not current.entity.position + Vec3(offset,0,0) in loaded:
        if current.entity.position + Vec3(offset,0,0) in chunks:
            chunks[current.entity.position + Vec3(offset,0,0)].enabled = True
            loaded[current.entity.position + Vec3(offset,0,0)] = chunks[current.entity.position + Vec3(offset,0,0)]
        else:
            terrain = TerrainChunk(offset=current.entity.position + Vec3(offset,0,0),texture='grass')
            terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
            chunks[terrain.position] = terrain
            loaded[terrain.position] = terrain
            print(terrain.position)
    if not current.entity.position + Vec3(-offset,0,0) in loaded:
        if current.entity.position + Vec3(-offset,0,0) in chunks:
            chunks[current.entity.position + Vec3(-offset,0,0)].enabled = True
            loaded[current.entity.position + Vec3(-offset,0,0)] = chunks[current.entity.position + Vec3(-offset,0,0)]
        else:
            terrain = TerrainChunk(offset=current.entity.position + Vec3(-offset,0,0),texture='grass')
            terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
            chunks[terrain.position] = terrain
            loaded[terrain.position] = terrain
            print(terrain.position)
    if not current.entity.position + Vec3(0,0,offset) in loaded:
        if current.entity.position + Vec3(0,0,offset) in chunks:
            chunks[current.entity.position + Vec3(0,0,offset)].enabled = True
            loaded[current.entity.position + Vec3(0,0,offset)] = chunks[current.entity.position + Vec3(0,0,offset)]
        else:
            terrain = TerrainChunk(offset=current.entity.position + Vec3(0,0,offset),texture='grass')
            terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
            chunks[terrain.position] = terrain
            loaded[terrain.position] = terrain
            print(terrain.position)
    if not current.entity.position + Vec3(0,0,-offset) in loaded:
        if current.entity.position + Vec3(0,0,-offset) in chunks:
            chunks[current.entity.position + Vec3(0,0,-offset)].enabled = True
            loaded[current.entity.position + Vec3(0,0,-offset)] = chunks[current.entity.position + Vec3(0,0,-offset)]
        else:
            terrain = TerrainChunk(offset=current.entity.position + Vec3(0,0,-offset),texture='grass')
            terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
            chunks[terrain.position] = terrain
            loaded[terrain.position] = terrain
            print(terrain.position)

    if not current.entity.position + Vec3(2*offset,0,0) in loaded:
        if current.entity.position + Vec3(2*offset,0,0) in chunks:
            chunks[current.entity.position + Vec3(2*offset,0,0)].enabled = True
            loaded[current.entity.position + Vec3(2*offset,0,0)] = chunks[current.entity.position + Vec3(2*offset,0,0)]
        else:
            terrain = TerrainChunk(offset=current.entity.position + Vec3(2*offset,0,0),texture='grass')
            terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
            chunks[terrain.position] = terrain
            loaded[terrain.position] = terrain
            print(terrain.position)
    if not current.entity.position + Vec3(-2*offset,0,0) in loaded:
        if current.entity.position + Vec3(-2*offset,0,0) in chunks:
            chunks[current.entity.position + Vec3(-2*offset,0,0)].enabled = True
            loaded[current.entity.position + Vec3(-2*offset,0,0)] = chunks[current.entity.position + Vec3(-2*offset,0,0)]
        else:
            terrain = TerrainChunk(offset=current.entity.position + Vec3(-2*offset,0,0),texture='grass')
            terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
            chunks[terrain.position] = terrain
            loaded[terrain.position] = terrain
            print(terrain.position)
    if not current.entity.position + Vec3(0,0,2*offset) in loaded:
        if current.entity.position + Vec3(0,0,2*offset) in chunks:
            chunks[current.entity.position + Vec3(0,0,2*offset)].enabled = True
            loaded[current.entity.position + Vec3(0,0,2*offset)] = chunks[current.entity.position + Vec3(0,0,2*offset)]
        else:
            terrain = TerrainChunk(offset=current.entity.position + Vec3(0,0,2*offset),texture='grass')
            terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
            chunks[terrain.position] = terrain
            loaded[terrain.position] = terrain
            print(terrain.position)
    if not current.entity.position + Vec3(0,0,-2*offset) in loaded:
        if current.entity.position + Vec3(0,0,-2*offset) in chunks:
            chunks[current.entity.position + Vec3(0,0,-2*offset)].enabled = True
            loaded[current.entity.position + Vec3(0,0,-2*offset)] = chunks[current.entity.position + Vec3(0,0,-2*offset)]
        else:
            terrain = TerrainChunk(offset=current.entity.position + Vec3(0,0,-2*offset),texture='grass')
            terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
            chunks[terrain.position] = terrain
            loaded[terrain.position] = terrain
            print(terrain.position)
    
    if not current.entity.position + Vec3(offset,0,offset) in loaded:
        if current.entity.position + Vec3(offset,0,offset) in chunks:
            chunks[current.entity.position + Vec3(offset,0,offset)].enabled = True
            loaded[current.entity.position + Vec3(offset,0,offset)] = chunks[current.entity.position + Vec3(offset,0,offset)]
        else:
            terrain = TerrainChunk(offset=current.entity.position + Vec3(offset,0,offset),texture='grass')
            terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
            chunks[terrain.position] = terrain
            loaded[terrain.position] = terrain
            print(terrain.position)
    if not current.entity.position + Vec3(offset,0,-offset) in loaded:
        if current.entity.position + Vec3(offset,0,-offset) in chunks:
            chunks[current.entity.position + Vec3(offset,0,-offset)].enabled = True
            loaded[current.entity.position + Vec3(offset,0,-offset)] = chunks[current.entity.position + Vec3(offset,0,-offset)]
        else:
            terrain = TerrainChunk(offset=current.entity.position + Vec3(offset,0,-offset),texture='grass')
            terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
            chunks[terrain.position] = terrain
            loaded[terrain.position] = terrain
            print(terrain.position)
    if not current.entity.position + Vec3(-offset,0,-offset) in loaded:
        if current.entity.position + Vec3(-offset,0,-offset) in chunks:
            chunks[current.entity.position + Vec3(-offset,0,-offset)].enabled = True
            loaded[current.entity.position + Vec3(-offset,0,-offset)] = chunks[current.entity.position + Vec3(-offset,0,-offset)]
        else:
            terrain = TerrainChunk(offset=current.entity.position + Vec3(-offset,0,-offset),texture='grass')
            terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
            chunks[terrain.position] = terrain
            loaded[terrain.position] = terrain
            print(terrain.position)
    if not current.entity.position + Vec3(-offset,0,offset) in loaded:
        if current.entity.position + Vec3(-100,0,100) in chunks:
            chunks[current.entity.position + Vec3(-100,0,100)].enabled = True
            loaded[current.entity.position + Vec3(-100,0,100)] = chunks[current.entity.position + Vec3(-100,0,100)]
        else:
            terrain = TerrainChunk(offset=current.entity.position + Vec3(-100,0,100),texture='grass')
            terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
            chunks[terrain.position] = terrain
            loaded[terrain.position] = terrain
            print(terrain.position)

def unload_chunks():
    for chunk in loaded:
        if distance(Vec3(player.x,0,player.z),chunk) > 100*3:
            loaded[chunk].enabled = False
            loaded.pop(chunk)
            break

app = Ursina()
chunks = {}
loaded = {}

for z in range(4):
    for x in range(4):
        terrain = TerrainChunk(offset=Vec3(x*100,0,z*100),texture='grass')
        terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
        chunks[terrain.position] = terrain
        loaded[terrain.position] = terrain
offset = 100
def tick_update():
    global player
    current = raycast(player,Vec3(0,-1,0),ignore=[player,])
    if current.hit:
        if current.entity.type == "terrain":
            thread1 = Thread(target=load_chunks,args=(current,))
            thread1.start()
            thread2 = Thread(target=unload_chunks)
            thread2.start()
            
    invoke(tick_update,delay=0.25)
            
player = FirstPersonController(model='cube',x=5,z=5,y=5)
player.speed = 20
tick_update() 
scene.fog_density = 0.01
Sky()
app.run()
