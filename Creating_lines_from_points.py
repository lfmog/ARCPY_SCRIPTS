import arcpy, os,sys, string,re, math

# ##ws = arcpy.env.workspace = arcpy.GetParameterAsText(0)
ws = arcpy.env.workspace =r"D:\PLAN_MANTENIMIENTO\MANTENIMIENTO_2022\VA\PROCESOS\Shp"
shp = 'SIN_PASO_CONSOLIDADO.shp'
shp_line = 'NEW_LINE.shp'
shp_ly = arcpy.MakeFeatureLayer_management(shp, "shp_ly")
shp_L_ly = arcpy.MakeFeatureLayer_management(shp_line, "shp_L_ly")
fields = ['LONGITUD', 'LATITUD', 'TRM_RML', 'TIPO_PK']
with arcpy.da.SearchCursor(shp_ly,fields) as in_rows:
    with arcpy.da.InsertCursor(shp_L_ly, ['SHAPE@'])as cursor:
        for row in in_rows:
            rowX = in_rows.next()
            rowX1 = float(rowX[0])
            rowY1 = float(rowX[1])
            rowT= rowX[2]
            rowTPK = rowX[3]
            if row[2] == rowT and (row[3]== '1' and rowTPK=='2'):
                # in_rows.reset()
                # build array for line segment
                print (row[0])
                print (rowX1)
                print (rowY1)
                array = arcpy.Array([arcpy.Point(row[0], row[1]), arcpy.Point(rowX1, rowY1)])
                # Create a Polyline object based on the array of points
                polyline = arcpy.Polyline(array)
                # Insert the feature
                cursor.insertRow([polyline])
            else:
                print("No encuentra pareja")
        # Delete cursor object
        del cursor
        print ("Procesado!")
