from ursina import *
from perlin_noise import PerlinNoise
from ursina.shaders import basic_lighting_shader
from ursina.prefabs.first_person_controller import FirstPersonController

def scale(val, src, dst):
    """
    Scale the given value from the scale of src to the scale of dst.
    """
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]


noise1 = PerlinNoise(1,random.randint(0,100000))
noise2 = PerlinNoise(1,random.randint(0,100000))
noise3 = PerlinNoise(1,random.randint(0,100000))

class TerrainChunk(Entity):
    def __init__(self,offset,**kwargs):
        self.xSize = 25
        self.zSise = 25
        self.height = 0
        self.depth = 0
        self.offset = offset
        self.type = 'terrain'

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
        vert = 0
        for z in range(self.zSise+1):
            for x in range(self.xSize+1):
                
                #y1 = noise1(((x+self.offset[0])*0.4,(z+self.offset[2])*0.4)) * 2
                #y2 = noise2(((x+self.offset[0])*0.1,(z+self.offset[2])*0.1)) * 10
                y3 = noise3(((x+self.offset[0])*0.02,(z+self.offset[2])*0.02)) * 7
                y = y3

                if y > self.height:
                    self.height = y
                if y < self.depth:
                    self.depth = y

                self.vertices.append(Vec3(x,y,z))
                self.uvs.append(Vec2(x/self.xSize,z/self.zSise))
                #yScaled = scale(y,(-20,20),(0,255))
                #self.colors.append(color.rgb(yScaled,yScaled,yScaled,255))

                if x < self.xSize and z < self.zSise:
                    self.triangles.extend([vert+0,vert+1,vert+self.xSize+2,vert+0,vert+self.xSize+2,vert+self.xSize+1])
                    vert += 1
            if x <= self.xSize and z <= self.zSise:
                vert += 1

app = Ursina()
# terrain1 = TerrainChunk(offset=Vec3(0,0,0),texture='grass')
# terrain2 = TerrainChunk(offset=Vec3(100,0,0),texture='grass')
# terrain1 = TerrainChunk(offset=Vec3(100,0,100),texture='grass')
# terrain2 = TerrainChunk(offset=Vec3(0,0,100),texture='grass')
chunks = {}
loaded = {}
for z in range(4):
    for x in range(4):
        terrain = TerrainChunk(offset=Vec3(x*25,0,z*25),texture='grass')
        terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
        chunks[terrain.position] = terrain
        loaded[terrain.position] = terrain

def update():
    global player
    current = raycast(player,Vec3(0,-1,0),ignore=[player,])
    if current.hit:
        if current.entity.type == "terrain":
            if not current.entity.position + Vec3(25,0,0) in loaded:
                if current.entity.position + Vec3(25,0,0) in chunks:
                    chunks[current.entity.position + Vec3(25,0,0)].enabled = True
                    loaded[current.entity.position + Vec3(25,0,0)] = chunks[current.entity.position + Vec3(25,0,0)]
                else:
                    terrain = TerrainChunk(offset=current.entity.position + Vec3(25,0,0),texture='grass')
                    terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
                    chunks[terrain.position] = terrain
                    loaded[terrain.position] = terrain
                    print(terrain.position)
            if not current.entity.position + Vec3(-25,0,0) in loaded:
                if current.entity.position + Vec3(-25,0,0) in chunks:
                    chunks[current.entity.position + Vec3(-25,0,0)].enabled = True
                    loaded[current.entity.position + Vec3(-25,0,0)] = chunks[current.entity.position + Vec3(-25,0,0)]
                else:
                    terrain = TerrainChunk(offset=current.entity.position + Vec3(-25,0,0),texture='grass')
                    terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
                    chunks[terrain.position] = terrain
                    loaded[terrain.position] = terrain
                    print(terrain.position)
            if not current.entity.position + Vec3(0,0,25) in loaded:
                if current.entity.position + Vec3(0,0,25) in chunks:
                    chunks[current.entity.position + Vec3(0,0,25)].enabled = True
                    loaded[current.entity.position + Vec3(0,0,25)] = chunks[current.entity.position + Vec3(0,0,25)]
                else:
                    terrain = TerrainChunk(offset=current.entity.position + Vec3(0,0,25),texture='grass')
                    terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
                    chunks[terrain.position] = terrain
                    loaded[terrain.position] = terrain
                    print(terrain.position)
            if not current.entity.position + Vec3(0,0,-25) in loaded:
                if current.entity.position + Vec3(0,0,-25) in chunks:
                    chunks[current.entity.position + Vec3(0,0,-25)].enabled = True
                    loaded[current.entity.position + Vec3(0,0,-25)] = chunks[current.entity.position + Vec3(0,0,-25)]
                else:
                    terrain = TerrainChunk(offset=current.entity.position + Vec3(0,0,-25),texture='grass')
                    terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
                    chunks[terrain.position] = terrain
                    loaded[terrain.position] = terrain
                    print(terrain.position)

            if not current.entity.position + Vec3(50,0,0) in loaded:
                if current.entity.position + Vec3(50,0,0) in chunks:
                    chunks[current.entity.position + Vec3(50,0,0)].enabled = True
                    loaded[current.entity.position + Vec3(50,0,0)] = chunks[current.entity.position + Vec3(50,0,0)]
                else:
                    terrain = TerrainChunk(offset=current.entity.position + Vec3(50,0,0),texture='grass')
                    terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
                    chunks[terrain.position] = terrain
                    loaded[terrain.position] = terrain
                    print(terrain.position)
            if not current.entity.position + Vec3(-50,0,0) in loaded:
                if current.entity.position + Vec3(-50,0,0) in chunks:
                    chunks[current.entity.position + Vec3(-50,0,0)].enabled = True
                    loaded[current.entity.position + Vec3(-50,0,0)] = chunks[current.entity.position + Vec3(-50,0,0)]
                else:
                    terrain = TerrainChunk(offset=current.entity.position + Vec3(-50,0,0),texture='grass')
                    terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
                    chunks[terrain.position] = terrain
                    loaded[terrain.position] = terrain
                    print(terrain.position)
            if not current.entity.position + Vec3(0,0,50) in loaded:
                if current.entity.position + Vec3(0,0,50) in chunks:
                    chunks[current.entity.position + Vec3(0,0,50)].enabled = True
                    loaded[current.entity.position + Vec3(0,0,50)] = chunks[current.entity.position + Vec3(0,0,50)]
                else:
                    terrain = TerrainChunk(offset=current.entity.position + Vec3(0,0,50),texture='grass')
                    terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
                    chunks[terrain.position] = terrain
                    loaded[terrain.position] = terrain
                    print(terrain.position)
            if not current.entity.position + Vec3(0,0,-50) in loaded:
                if current.entity.position + Vec3(0,0,-50) in chunks:
                    chunks[current.entity.position + Vec3(0,0,-50)].enabled = True
                    loaded[current.entity.position + Vec3(0,0,-50)] = chunks[current.entity.position + Vec3(0,0,-50)]
                else:
                    terrain = TerrainChunk(offset=current.entity.position + Vec3(0,0,-50),texture='grass')
                    terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
                    chunks[terrain.position] = terrain
                    loaded[terrain.position] = terrain
                    print(terrain.position)
            
            if not current.entity.position + Vec3(25,0,25) in loaded:
                if current.entity.position + Vec3(25,0,25) in chunks:
                    chunks[current.entity.position + Vec3(25,0,25)].enabled = True
                    loaded[current.entity.position + Vec3(25,0,25)] = chunks[current.entity.position + Vec3(25,0,25)]
                else:
                    terrain = TerrainChunk(offset=current.entity.position + Vec3(25,0,25),texture='grass')
                    terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
                    chunks[terrain.position] = terrain
                    loaded[terrain.position] = terrain
                    print(terrain.position)
            if not current.entity.position + Vec3(25,0,-25) in loaded:
                if current.entity.position + Vec3(25,0,-25) in chunks:
                    chunks[current.entity.position + Vec3(25,0,-25)].enabled = True
                    loaded[current.entity.position + Vec3(25,0,-25)] = chunks[current.entity.position + Vec3(25,0,-25)]
                else:
                    terrain = TerrainChunk(offset=current.entity.position + Vec3(25,0,-25),texture='grass')
                    terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
                    chunks[terrain.position] = terrain
                    loaded[terrain.position] = terrain
                    print(terrain.position)
            if not current.entity.position + Vec3(-25,0,-25) in loaded:
                if current.entity.position + Vec3(-25,0,-25) in chunks:
                    chunks[current.entity.position + Vec3(-25,0,-25)].enabled = True
                    loaded[current.entity.position + Vec3(-25,0,-25)] = chunks[current.entity.position + Vec3(-25,0,-25)]
                else:
                    terrain = TerrainChunk(offset=current.entity.position + Vec3(-25,0,-25),texture='grass')
                    terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
                    chunks[terrain.position] = terrain
                    loaded[terrain.position] = terrain
                    print(terrain.position)
            if not current.entity.position + Vec3(-25,0,25) in loaded:
                if current.entity.position + Vec3(-25,0,25) in chunks:
                    chunks[current.entity.position + Vec3(-25,0,25)].enabled = True
                    loaded[current.entity.position + Vec3(-25,0,25)] = chunks[current.entity.position + Vec3(-25,0,25)]
                else:
                    terrain = TerrainChunk(offset=current.entity.position + Vec3(-25,0,25),texture='grass')
                    terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
                    chunks[terrain.position] = terrain
                    loaded[terrain.position] = terrain
                    print(terrain.position)

            
            # if not current.entity.position + Vec3(50,0,50) in loaded:
            #     if current.entity.position + Vec3(50,0,50) in chunks:
            #         chunks[current.entity.position + Vec3(50,0,50)].enabled = True
            #         loaded[current.entity.position + Vec3(50,0,50)] = chunks[current.entity.position + Vec3(50,0,50)]
            #     else:
            #         terrain = TerrainChunk(offset=current.entity.position + Vec3(50,0,50),texture='grass')
            #         terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
            #         chunks[terrain.position] = terrain
            #         loaded[terrain.position] = terrain
            #         print(terrain.position)
            # if not current.entity.position + Vec3(50,0,-50) in loaded:
            #     if current.entity.position + Vec3(50,0,-50) in chunks:
            #         chunks[current.entity.position + Vec3(50,0,-50)].enabled = True
            #         loaded[current.entity.position + Vec3(50,0,-50)] = chunks[current.entity.position + Vec3(50,0,-50)]
            #     else:
            #         terrain = TerrainChunk(offset=current.entity.position + Vec3(50,0,-50),texture='grass')
            #         terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
            #         chunks[terrain.position] = terrain
            #         loaded[terrain.position] = terrain
            #         print(terrain.position)
            # if not current.entity.position + Vec3(-50,0,-50) in loaded:
            #     if current.entity.position + Vec3(-50,0,-50) in chunks:
            #         chunks[current.entity.position + Vec3(-50,0,-50)].enabled = True
            #         loaded[current.entity.position + Vec3(-50,0,-50)] = chunks[current.entity.position + Vec3(-50,0,-50)]
            #     else:
            #         terrain = TerrainChunk(offset=current.entity.position + Vec3(-50,0,-50),texture='grass')
            #         terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
            #         chunks[terrain.position] = terrain
            #         loaded[terrain.position] = terrain
            #         print(terrain.position)
            # if not current.entity.position + Vec3(-50,0,50) in loaded:
            #     if current.entity.position + Vec3(-50,0,50) in chunks:
            #         chunks[current.entity.position + Vec3(-50,0,50)].enabled = True
            #         loaded[current.entity.position + Vec3(-50,0,50)] = chunks[current.entity.position + Vec3(-50,0,50)]
            #     else:
            #         terrain = TerrainChunk(offset=current.entity.position + Vec3(-50,0,50),texture='grass')
            #         terrain.collider = MeshCollider(terrain,terrain.model,terrain.position)
            #         chunks[terrain.position] = terrain
            #         loaded[terrain.position] = terrain
            #         print(terrain.position)
        
            for chunk in loaded:
                if distance(player.position,chunk) > 25*3:
                    loaded[chunk].enabled = False
                    loaded.pop(chunk)
                    break
            
player = FirstPersonController(model='cube',x=5,z=5,y=5)
scene.fog_density = 0.01
Sky()
app.run()