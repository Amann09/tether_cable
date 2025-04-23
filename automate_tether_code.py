def generate_segment(i):
    next_i = i + 1
    return f"""
<link name="cylinder_{i}">
    <pose relative_to='sphere_{i - 1}'>0 0 -0.1025 0 0 0</pose>
    <visual name='cylinder_{i} visual'>
        <pose>0 0 0 0 0 0</pose>
        <geometry>
            <cylinder>
                <radius>0.0025</radius>
                <length>0.2</length>
            </cylinder>
        </geometry>
        <material>
            <ambient>1 0 0 1</ambient>
            <diffuse>1 0 0 1</diffuse>
            <specular>0.1 0.1 0.1 1</specular>
            <emissive>0 0 0 1</emissive>
        </material>
    </visual>
    <collision name='cylinder_{i} collision'>
        <pose>0 0 0 0 0 0</pose>
        <geometry>
            <cylinder>
                <radius>0.0025</radius>
                <length>0.2</length>
            </cylinder>
        </geometry>
    </collision>
    <inertial>
        <mass>0.001</mass>
        <inertia>
            <ixx>0.01</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>0.01</iyy>
            <iyz>0</iyz>
            <izz>0.01</izz>
        </inertia>
    </inertial>
</link>
<joint name="sphere_{i - 1}_to_cylinder_{i}" type="universal">
    <pose relative_to='sphere_{i - 1}'>0 0 0 0 0 0</pose>
    <child>cylinder_{i}</child>
    <parent>sphere_{i - 1}</parent>
    <axis>
        <xyz>0 1 0</xyz>
        <limit>
            <lower>-1.57</lower>
            <upper>1.57</upper>
        </limit>
        <dynamics>
            <damping>1.0</damping>
        </dynamics>
        <use_parent_model_frame>true</use_parent_model_frame>
    </axis>
    <axis2>
        <xyz>0 0 1</xyz>
        <limit>
            <lower>-1.57</lower>
            <upper>1.57</upper>
        </limit>
        <dynamics>
            <damping>1.0</damping>
        </dynamics>
        <use_parent_model_frame>true</use_parent_model_frame>
    </axis2>
    <physics>
        <ode>
            <cfm_damping>1</cfm_damping>
        </ode>
    </physics>
</joint>
<link name="sphere_{i}">
    <pose relative_to='cylinder_{i}'>0 0 -0.1025 0 0 0</pose>
    <visual name='sphere_{i} visual'>
        <pose>0 0 0 0 0 0</pose>
        <geometry>
            <sphere>
                <radius>0.0025</radius>
            </sphere>
        </geometry>
        <material>
            <ambient>0 1 0.001214107934117647 1</ambient>
            <diffuse>0 1 0.001214107934117647 1</diffuse>
            <specular>0.1 0.1 0.1 1</specular>
            <emissive>0 0 0 1</emissive>
        </material>
    </visual>
    <collision name='sphere_{i} collision'>
        <pose>0 0 0 0 0 0</pose>
        <geometry>
            <sphere>
                <radius>0.0025</radius>
            </sphere>
        </geometry>
    </collision>
</link>
<joint name="cylinder_{i}_to_sphere_{i}" type="universal">
    <pose relative_to='sphere_{i}'>0 0 0 0 0 0</pose>
    <child>sphere_{i}</child>
    <parent>cylinder_{i}</parent>
    <axis>
        <xyz>0 1 0</xyz>
        <limit>
            <lower>-1.57</lower>
            <upper>1.57</upper>
        </limit>
        <dynamics>
            <damping>1.0</damping>
        </dynamics>
        <use_parent_model_frame>true</use_parent_model_frame>
    </axis>
    <axis2>
        <xyz>0 0 1</xyz>
        <limit>
            <lower>-1.57</lower>
            <upper>1.57</upper>
        </limit>
        <dynamics>
            <damping>1.0</damping>
        </dynamics>
        <use_parent_model_frame>true</use_parent_model_frame>
    </axis2>
    <physics>
        <ode>
            <cfm_damping>1</cfm_damping>
        </ode>
    </physics>
</joint>
"""

# Generate segments from 6 to 45 (since you already have up to 5)
for i in range(6, 11):
    print(generate_segment(i))
