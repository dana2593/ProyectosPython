-- =============================================
-- Author:		Geovanni Aucancela
-- Create date: 2025/02/02
-- Description:	SP, Listar Alumnos
-- =============================================
drop procedure sp_ListadoAlumnos
GO

ALTER PROCEDURE sp_ListadoEstudiantes
	@id_empleado int 
AS
BEGIN
	 BEGIN TRY
			 IF EXISTS (SELECT TOP 1 IDEstudiante FROM Estudiantes WHERE IDEstudiante=@id_empleado)
				SELECT EST.NombreEstudiante,EST.ApellidoEstudiante,EST.Email
				FROM Estudiantes EST
				WHERE EST.IDEstudiante=@id_empleado
		    ELSE
				BEGIN
					-- Estudiante no encontrado
					THROW 50001, 'SQL SERVER: ID de Estudiante NO Existe', 1;
				END
				
	 END TRY

    BEGIN CATCH
        -- Manejo de errores
        SELECT 
            ERROR_NUMBER() AS ErrorNumber,
            ERROR_MESSAGE() AS ErrorSQLServer;
            --ERROR_SEVERITY() AS ErrorSeverity,
            --ERROR_STATE() AS ErrorState,
            --ERROR_LINE() AS ErrorLine,
            --ERROR_PROCEDURE() AS ErrorProcedure;
    END CATCH
END
GO

EXECUTE sp_ListadoEstudiantes 99



 CREATE PROCEDURE sp_EliminarProducto
 @idproducto INT
 AS
 BEGIN
 BEGIN TRY
 IF NOT EXISTS (SELECT TOP 1 ProductID FROM Products WHERE ProductID = @idproducto)
 BEGIN
 THROW 50001, 'ID Producto no Existe.', 1;
 END
 DELETE FROM Products WHERE ProductID = @idproducto
 END TRY
    BEGIN CATCH
        -- Manejo de errores
        SELECT 
            ERROR_NUMBER() AS ErrorNumber,
            ERROR_MESSAGE() AS ErrorMessage,
            ERROR_SEVERITY() AS ErrorSeverity,
            ERROR_STATE() AS ErrorState,
            ERROR_LINE() AS ErrorLine,
            ERROR_PROCEDURE() AS ErrorProcedure;
        PRINT 'Ocurrió un error al intentar Eliminar el Producto.';
    END CATCH
 END
